import os
import numpy as np
import pydicom
from skimage import measure
import trimesh

# Crear carpeta de salida si no existe
def crear_directorio_salida(output_folder: str) -> None:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

# Leer y ordenar archivos DICOM por posición en el eje Z
def leer_dicoms(dicom_folder: str) -> list:
    dicoms = [pydicom.dcmread(os.path.join(dicom_folder, f))
              for f in os.listdir(dicom_folder) if f.endswith('.dcm')]
    dicoms.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    return dicoms

# Convertir imágenes DICOM a volumen en unidades Hounsfield (HU)
def convertir_a_hu(slices: list) -> np.ndarray:
    volume = np.stack([s.pixel_array for s in slices]).astype(np.int16)
    for i, s in enumerate(slices):
        intercept = s.RescaleIntercept
        slope = s.RescaleSlope
        volume[i] = volume[i] * slope + intercept
    return volume

# Crear máscara de hueso según un umbral dado
def crear_mascara_hueso(volume: np.ndarray, threshold: int) -> np.ndarray:
    return volume > threshold

# Generar malla 3D a partir de la máscara
def generar_malla(mask: np.ndarray) -> trimesh.Trimesh:
    verts, faces, normals, _ = measure.marching_cubes(mask, level=0)
    return trimesh.Trimesh(vertices=verts, faces=faces, vertex_normals=normals)

# Exportar malla 3D a archivo STL
def exportar_stl(mesh: trimesh.Trimesh, output_path: str) -> None:
    mesh.export(output_path)
    print(f"Exportado: {output_path}")

# Función principal que organiza todo el flujo
def dicom_to_stl_bone(dicom_folder: str, output_folder: str, stl_filename: str = "output", bone_threshold: int = 300) -> None:
    crear_directorio_salida(output_folder)
    slices = leer_dicoms(dicom_folder)
    volume = convertir_a_hu(slices)
    bone_mask = crear_mascara_hueso(volume, bone_threshold)
    mesh = generar_malla(bone_mask)
    output_stl_file = os.path.join(output_folder, f"{stl_filename}.stl")
    exportar_stl(mesh, output_stl_file)

# Ejemplo de uso
dicom_folder = r"C:\Users\MSI\Downloads\RADIOGRAFIAS\COLUMNA LUMBRAR\2597 SOLANO CHUQUILLANQUI EDITH\CT Cuerpo 1.0"
output_folder = r"C:\Users\MSI\Downloads\RADIOGRAFIAS\STL CONVERTIDOS"
stl_filename = "SOLANO CHUQUILLANQUI EDITH"

dicom_to_stl_bone(dicom_folder, output_folder, stl_filename)
