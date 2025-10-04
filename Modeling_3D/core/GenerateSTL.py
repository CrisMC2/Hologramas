import os
import numpy as np
import pydicom as dc
import trimesh

from typing import Union, overload
from skimage import measure

from skimage.filters import gaussian, median

from Shared.classes.ExistsPath import ExistsPath
from Modeling_3D.config import constantGenerateSTL as consGenStl


class GenerateSTL():
    def __init__(self, bone_threshold: int = 
                 consGenStl.BONE_THRESHOLD):

        self.bone_threshold = bone_threshold
        
        self.exists_path = ExistsPath()

    # Leer y ordenar archivos DICOM por posición en el eje Z
    def leer_dicoms(self, dicom_folder: str) -> list:
        dicoms = [dc.dcmread(os.path.join(dicom_folder, f))
                for f in os.listdir(dicom_folder) if f.endswith('.dcm')]
        
        dicoms.sort(key=lambda x: float(x.ImagePositionPatient[2]))
        return dicoms

    # Convertir imágenes DICOM a volumen en unidades Hounsfield (HU)
    def convertir_a_hu(self, slices: np.ndarray) -> np.ndarray:
        # volume = np.stack([s.pixel_array for s in slices]).astype(np.int16)
        volume = np.stack([s.pixel_array[:380,:] for s in slices]).astype(np.int16)
        
        volume_float_hu = volume.astype(np.float32)

        # Aplicar un filtro (ejemplo con Gaussiano)
        # sigma = 1.0
        # filtered_volume_float = gaussian(volume_float, sigma=sigma, channel_axis=None) # Si es una imagen 2D
        # Para volumen 3D:
        sigma_3d = (0.3, 0.3, 0.3) # sigma para cada eje (z, y, x)
        filtered_volume_float_hu = gaussian(volume_float_hu, sigma=sigma_3d, preserve_range=True) # preserve_range=True para mantener el rango de HU

        # 2. Convertir de nuevo a int16 si es necesario
        # Asegúrate de que los valores resultantes estén dentro del rango de int16
        # y maneja el redondeo.
        volume = np.round(filtered_volume_float_hu).astype(np.int16)

        for i, s in enumerate(slices):
            intercept = s.RescaleIntercept
            slope = s.RescaleSlope
            volume[i] = volume[i] * slope + intercept
        return volume

    # Crear máscara de hueso según un umbral dado
    def crear_mascara_hueso(self, volume: np.ndarray, 
                            threshold: int) -> np.ndarray:
        return volume > threshold

    # Generar malla 3D a partir de la máscara
    def generar_malla(self, mask: np.ndarray) -> trimesh.Trimesh:
        verts, faces, normals, _ = measure.marching_cubes(mask, level=0)
        return trimesh.Trimesh(vertices=verts, faces=faces, vertex_normals=normals)

    # Exportar malla 3D a archivo STL
    def exportar_stl(self, mesh: trimesh.Trimesh, output_path: str, stl_filename: str="Output") -> None:
        output_stl_file = os.path.join(output_path, f"{stl_filename}.stl")
        mesh.export(output_stl_file)
        print(f"Exportado: {output_stl_file}")
    
    @overload
    def execute(self, dicoms: Union[str, list]) -> None: ...
    @overload
    def execute(self, dicoms: Union[str, list], output_folder: str, stl_filename: str="Output") -> None: ...

    # Función principal que organiza todo el flujo
    def execute(self, dicoms: Union[str, list], output_folder: str=None, stl_filename: str="Output") -> None:
        # if self.exists_path.exists(output_folder):
            
            if isinstance(dicoms, str):
                slices = self.leer_dicoms(dicom_folder=dicoms)
            
            elif isinstance(dicoms, list):
                slices = dicoms
                
            volume = self.convertir_a_hu(slices=slices)
            bone_mask = self.crear_mascara_hueso(volume=volume, 
                                                 threshold=self.bone_threshold)
            mesh = self.generar_malla(bone_mask)
            
            if output_folder:
                self.exportar_stl(mesh=mesh, output_path=output_folder, 
                              stl_filename=stl_filename)
            
            return mesh

# Ejemplo de uso
dicom_folder = r"C:\Users\MSI\Downloads\RADIOGRAFIAS\COLUMNA LUMBRAR\2597 SOLANO CHUQUILLANQUI EDITH\CT Cuerpo 1.0"
output_folder = r"C:\Users\MSI\Downloads\RADIOGRAFIAS\STL CONVERTIDOS"
stl_filename = "SOLANO CHUQUILLANQUI EDITH"

# dicom_to_stl_bone(dicom_folder, output_folder, stl_filename)