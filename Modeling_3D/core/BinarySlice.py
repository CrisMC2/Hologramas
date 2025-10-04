# ... (tu clase GenerateSTL y su implementación) ...

import os
import numpy as np
import trimesh
from PIL import Image, ImageDraw
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
log = logging.getLogger(__name__)


class SlicerForLightCrafter:
    def __init__(self, mesh: trimesh.Trimesh, output_dir: str = "sliced_patterns"):
        self.mesh = mesh
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        mesh_extents = mesh.extents # e.g., np.array([490., 314., 460.]) en mm
        log.info(f"Dimensiones de la malla (X, Y, Z): {mesh_extents} mm")

    def slice_mesh(self, num_slices: int, resolution_xy: tuple = (1024, 768)) -> list[np.ndarray]:
        """
        Genera una serie de rebanadas binarias 2D de la malla 3D.

        Args:
            num_slices (int): Número de rebanadas a generar a lo largo del eje Z.
            resolution_xy (tuple): Resolución (ancho, alto) de las imágenes de las rebanadas.

        Returns:
            list[np.ndarray]: Una lista de arrays NumPy, donde cada array es una imagen binaria 2D.
        """
        
        # 1. Obtener los límites de la malla en el eje Z
        # self.mesh.bounds devuelve [[min_x, min_y, min_z], [max_x, max_y, max_z]]
        min_z = self.mesh.bounds[0, 2]
        max_z = self.mesh.bounds[1, 2]
        
        # Calcular el espaciado entre rebanadas
        z_step = (max_z - min_z) / (num_slices - 1) if num_slices > 1 else 0

        sliced_images = []
        print(f"Generando {num_slices} rebanadas binarias...")

        for i in range(num_slices):
            current_z = min_z + i * z_step

            # 2. Realizar el corte (slice) de la malla
            # trimesh.section: crea una sección transversal de la malla con un plano
            # El plano se define por un origen (un punto en el plano) y una normal (la dirección del plano)
            # Aquí, el plano es perpendicular al eje Z, así que la normal es [0,0,1]
            # y el origen está en la altura actual_z
            
            # Obtener el objeto Path2D de la sección
            section_2d = self.mesh.section(plane_origin=[0, 0, current_z], plane_normal=[0, 0, 1])

            if section_2d is None:
                # No hay intersección en esta altura
                binary_image = np.zeros(resolution_xy[::-1], dtype=np.uint8) # Genera una imagen negra
            else:
                # 3. Renderizar el corte en una imagen binaria
                # Convertir el Path2D a un polígono para renderizarlo
                # Puede haber múltiples componentes si el corte atraviesa agujeros, etc.
                polygons_2d = []
                for entity in section_2d.entities:
                    if isinstance(entity, trimesh.path.path.Path):
                        # Convertir segmentos de camino a polígonos
                        polygons_2d.extend(entity.polygons)
                    elif isinstance(entity, trimesh.path.polygons.Polygon):
                        polygons_2d.append(entity)

                if not polygons_2d:
                    binary_image = np.zeros(resolution_xy[::-1], dtype=np.uint8) # Imagen negra si no hay polígonos
                else:
                    # Crear una imagen en blanco y dibujar los polígonos
                    # Esto requiere una librería de dibujo 2D. Pillow es una buena opción.
                    # Asegúrate de que los polígonos estén en coordenadas de píxeles
                    
                    # Calcular el factor de escala y desplazamiento para mapear coordenadas 3D a píxeles 2D
                    # Esto dependerá de la extensión de tu malla en X e Y
                    mesh_min_x, mesh_min_y = self.mesh.bounds[0, 0], self.mesh.bounds[0, 1]
                    mesh_max_x, mesh_max_y = self.mesh.bounds[1, 0], self.mesh.bounds[1, 1]
                    
                    # Asegurarse de que el aspect ratio se mantenga o que la imagen se ajuste correctamente
                    # Si la relación de aspecto no se mantiene, la forma podría distorsionarse.
                    # Aquí asumimos que queremos ajustar la sección dentro del tamaño de la imagen,
                    # manteniendo el aspecto de la sección.
                    
                    range_x = mesh_max_x - mesh_min_x
                    range_y = mesh_max_y - mesh_min_y
                    
                    if range_x == 0: range_x = 1 # Evitar división por cero
                    if range_y == 0: range_y = 1

                    scale_x = resolution_xy[0] / range_x
                    scale_y = resolution_xy[1] / range_y
                    
                    # Usar el factor de escala más pequeño para asegurar que el contenido quepa
                    # o un factor de escala independiente si la distorsión es aceptable
                    # Para mantener el aspecto, podríamos usar:
                    # scale_factor = min(scale_x, scale_y)
                    # offset_x = -mesh_min_x * scale_factor
                    # offset_y = -mesh_min_y * scale_factor
                    # O simplemente mapear directamente, lo que puede distorsionar si el aspecto no coincide:

                    image = Image.new('1', resolution_xy, color=0) # '1' para binario (blanco y negro)
                    draw = ImageDraw.Draw(image)
                    
                    for poly in polygons_2d:
                        # Convertir vértices de polígono a coordenadas de imagen
                        # Ajustar la escala y el origen para que encaje en la imagen
                        # Esto es una simplificación; para una buena calidad, necesitarías un renderizador más sofisticado
                        # o una gestión de coordenadas más precisa.
                        points_scaled = []
                        for point in poly.exterior.coords:
                            # Mapear X, Y a coordenadas de píxel
                            px = int((point[0] - mesh_min_x) * scale_x)
                            py = int((point[1] - mesh_min_y) * scale_y) # Y suele estar invertido en imágenes
                            points_scaled.append((px, py))
                        
                        # Asegurarse de que los puntos estén dentro de los límites de la imagen
                        points_scaled = [(max(0, min(resolution_xy[0]-1, x)), max(0, min(resolution_xy[1]-1, y))) for x, y in points_scaled]
                        
                        if len(points_scaled) > 1: # Asegurarse de que hay suficientes puntos para un polígono
                            draw.polygon(points_scaled, fill=1) # Dibuja el polígono, rellénalo con blanco (1)

                    binary_image = np.array(image, dtype=np.uint8) * 255 # Convertir a 0/255 para fácil visualización/uso
            
            sliced_images.append(binary_image)
            
            # Opcional: Guardar la imagen para verificar
            output_filepath = os.path.join(self.output_dir, f"slice_{i:04d}.png")
            Image.fromarray(binary_image).save(output_filepath)
            
            print(f"  Rebanada {i+1}/{num_slices} generada en Z={current_z:.2f}. Guardada como {output_filepath}")

        return sliced_images
    
    


    def binarize_mesh_by_surface_voxelization(self, pitch: float, output_dir: str = "voxel_slices_skeleton_1"):
        mesh = self.mesh
        os.makedirs(output_dir, exist_ok=True)

        log.info(f"Iniciando voxelización de la superficie de la malla con pitch={pitch}...")

        # Voxelizar la malla. Esto crea un objeto VoxelGrid
        # El método 'ray' o 'subdivide' funciona bien para la superficie.
        # NO usaremos .fill() después, ya que la malla no es estanca por naturaleza.
        # `pad=1` asegura que los voxels en los bordes de la malla se capturen completamente.
        voxels = mesh.voxelized(pitch=pitch, method='ray') 

        log.info(f"Malla voxelizada a una cuadrícula con dimensiones: {voxels.shape}")

        # Convertir el objeto VoxelGrid a un array NumPy binario (0s y 1s o 0s y 255s)
        # `matrix` es un array booleano, convertimos a uint8 para 0/255 para las imágenes
        volume_data = voxels.matrix.astype(np.uint8) * 255
        
        log.info(f"Volumen de voxels binario generado con forma (Z, Y, X): {volume_data.shape}")

        # Extraer y guardar los slices 2D del volumen de voxels
        num_slices = volume_data.shape[0] 

        log.info(f"Extrayendo {num_slices} rebanadas binarias del volumen de voxels...")

        # Aquí también necesitamos ajustar el escalado y offset para las imágenes finales,
        # similar a como lo hacíamos con section(), pero ahora mapeando los voxels.
        # Los límites del volumen de voxels están en `voxels.bounds`.
        voxel_min_x, voxel_min_y, voxel_min_z = voxels.bounds[0]
        voxel_max_x, voxel_max_y, voxel_max_z = voxels.bounds[1]

        # La resolución de las imágenes debe coincidir con la resolución XY de los voxels
        # o ser escalada para el DLP.
        # Para que los slices directamente del volumen de voxels tengan sentido:
        # resolution_xy_for_voxels = (volume_data.shape[2], volume_data.shape[1]) # (X, Y)
        # Si la resolución del DLP es diferente:
        dlp_resolution_x, dlp_resolution_y = 1024, 768 # Tu resolución deseada para el DLP
        dlp_resolution_x, dlp_resolution_y = 640, 480 # Tu resolución deseada para el DLP


        # Calcula la escala para mapear la extensión de los voxels a la resolución DLP
        scale_x = dlp_resolution_x / (voxel_max_x - voxel_min_x)
        scale_y = dlp_resolution_y / (voxel_max_y - voxel_min_y)

        # Para mantener el aspecto y centrar:
        uniform_scale = min(scale_x, scale_y)
        offset_x = (dlp_resolution_x / 2) - ((voxel_min_x + voxel_max_x) / 2) * uniform_scale
        offset_y = (dlp_resolution_y / 2) - ((voxel_min_y + voxel_max_y) / 2) * uniform_scale


        for i in range(num_slices):
            # Obtener el slice binario de 0/255
            slice_2d_raw = volume_data[i, :, :] 

            # Crear una imagen PIL a partir del slice.
            # Convertir a 'L' (escala de grises) y luego a '1' (binario) para Pillow
            # La transposición de slice_2d_raw puede ser necesaria dependiendo de cómo se orientó el volumen
            # Si el slice es (Y, X), y Pillow espera (X, Y) para image.size

            # Asegúrate de que la orientación sea correcta (PIL espera width, height)
            # volume_data.shape es (Z, Y, X)
            # slice_2d_raw es (Y, X)
            # image.size espera (width, height) == (X, Y)
            # Por lo tanto, necesitamos transponer si los ejes XY no están en el orden deseado por PIL
            # O simplemente crear una imagen con las dimensiones correctas y dibujar directamente

            # Mejor enfoque: Crear una imagen en blanco y dibujar los puntos voxel a voxel.
            # Esto da más control sobre el mapeo al tamaño del DLP.

            image_pil = Image.new('1', (dlp_resolution_x, dlp_resolution_y), color=0)
            draw = ImageDraw.Draw(image_pil)

            # Iterar sobre los voxels activos en el slice
            # np.where devuelve las coordenadas (filas, columnas) de los elementos True (255)
            y_coords, x_coords = np.where(slice_2d_raw == 255)

            for y, x in zip(y_coords, x_coords):
                # Calcular la posición en píxeles de la imagen DLP
                # Aquí 'x' e 'y' son las coordenadas del voxel en su matriz 2D.
                # Necesitamos mapear estas coordenadas relativas al volumen completo
                # a la imagen DLP.
                
                # --- Añade estas líneas de depuración ---
                log.info(f"DEBUG: Tipo de x_coords: {type(x_coords)}, Forma: {x_coords.shape}")
                log.info(f"DEBUG: Tipo de y_coords: {type(y_coords)}, Forma: {y_coords.shape}")
                log.info(f"DEBUG: Tipo de voxels.pitch: {type(voxels.pitch)}, Valor: {voxels.pitch}")
                
                # --- Fin de depuración ---
                x_scalar = float(x)
                y_scalar = float(y)

                actual_pitch_value = float(voxels.pitch[0]) 

                # Coordenadas 3D relativas al origen del volumen de voxels
                coord_x_3d = voxel_min_x + x_scalar * actual_pitch_value
                coord_y_3d = voxel_min_y + y_scalar * actual_pitch_value

                # Mapear a píxeles de la imagen DLP con el factor de escala uniforme
                px = int(coord_x_3d * uniform_scale + offset_x)
                py = int(coord_y_3d * uniform_scale + offset_y)

                # Dibujar un pequeño cuadrado o un punto para cada voxel
                # Puedes dibujar un círculo o un rectángulo para representar el voxel
                # Aquí, dibujamos un píxel simple (o un cuadrado si el voxel es grande en pantalla)
                # Asegúrate de que las coordenadas estén dentro de los límites de la imagen
                px = max(0, min(dlp_resolution_x - 1, px))
                py = max(0, min(dlp_resolution_y - 1, py))

                # Dibuja un cuadrado de 1x1 píxel para cada voxel
                draw.point((px, py), fill=1) 
                # Si quieres que los voxels sean visibles como cuadrados más grandes,
                # podrías dibujar draw.rectangle([px, py, px+voxel_display_size, py+voxel_display_size], fill=1)
                # donde voxel_display_size es un cálculo basado en pitch y uniform_scale.

            binary_image = np.array(image_pil, dtype=np.uint8) * 255 

            output_filepath = os.path.join(output_dir, f"voxel_slice_{i:04d}.jpg")
            Image.fromarray(binary_image).save(output_filepath)
            log.info(f"  Voxel Slice {i+1}/{num_slices} guardada como {output_filepath}")

        log.info("Binarización por voxelización de superficie completada y slices guardados.")
        return volume_data






















# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Necesitas tu clase GenerateSTL aquí para obtener la malla
    # Esto es un placeholder; asegúrate de que 'consGenStl' y 'ExistsPath' estén disponibles
    
    # Simulación de una malla trimesh (reemplaza esto con la salida de tu GenerateSTL)
    # Por ejemplo, cargando un STL existente
    try:
        from Modeling_3D.config import constantGenerateSTL as consGenStl # Asegúrate de que esto sea accesible
        from Shared.classes.ExistsPath import ExistsPath # Asegúrate de que esto sea accesible
        from pydicom import dcmread # Solo para el tipo de dato, no para usarlo realmente aquí

        # Crear una instancia de GenerateSTL
        class_gen_stl = GenerateSTL() 
        
        # Cargar DICOMs y generar la malla 
        # Asegúrate de reemplazar 'path_to_your_dicom_folder' con la ruta real a tus archivos DICOM
        # Y 'path_to_output_stl' con la carpeta donde se guardará el STL temporalmente
        dicom_folder_path = "path_to_your_dicom_folder" 
        output_stl_path = "path_to_output_stl" 

        # Asegúrate de que las rutas existan
        os.makedirs(output_stl_path, exist_ok=True)
        # os.makedirs(dicom_folder_path, exist_ok=True) # Asegúrate de que esta carpeta exista con tus DICOMs

        if not os.path.exists(dicom_folder_path) or not any(f.endswith('.dcm') for f in os.listdir(dicom_folder_path)):
            print(f"AVISO: La carpeta DICOM '{dicom_folder_path}' no existe o no contiene archivos .dcm.")
            print("Generando una malla de ejemplo para la demostración.")
            # Si no hay DICOMs, genera una malla de ejemplo (una esfera)
            mesh = trimesh.creation.icosphere(subdivisions=2, radius=10.0)
            # Asegúrate de ajustar las bounds si usas una esfera de ejemplo vs un hueso real
            # Para un DLP LightCrafter, es importante que tu malla esté escalada a un tamaño "real"
            # por ejemplo, en milímetros, y luego mapees eso a la resolución del proyector.
            # Aquí, la esfera de radio 10 es solo un ejemplo conceptual.
        else:
            print(f"Procesando DICOMs desde: {dicom_folder_path}")
            mesh = class_gen_stl.execute(dicoms=dicom_folder_path, output_folder=output_stl_path, stl_filename="reconstruccion_hueso")

        # Verifica que la malla se generó correctamente
        if mesh is None or not isinstance(mesh, trimesh.Trimesh):
            raise ValueError("No se pudo generar la malla 3D. Asegúrate de que tus DICOMs sean válidos y el threshold sea correcto.")

        # Ahora que tenemos la malla, la pasamos al slicer
        slicer = SlicerForLightCrafter(mesh=mesh)

        # Configura la resolución de los patrones que tu DLP LightCrafter soporta
        # Por ejemplo, DLP LightCrafter 4500 tiene una resolución nativa de 912x1140 o 800x600, etc.
        # ¡IMPORTANTE! Ajusta esto a la resolución real de tu DMD del LightCrafter
        DMD_WIDTH = 640  # Ejemplo: Ancho del chip DMD
        DMD_HEIGHT = 480 # Ejemplo: Alto del chip DMD

        num_slices_to_project = 100 # Puedes ajustar el número de rebanadas
        
        # Asegúrate de instalar Pillow: pip install Pillow
        from PIL import ImageDraw 

        binary_slices = slicer.slice_mesh(
            num_slices=num_slices_to_project,
            resolution_xy=(DMD_WIDTH, DMD_HEIGHT)
        )

        print(f"\nGeneradas {len(binary_slices)} imágenes binarias.")
        print(f"Las imágenes están guardadas en: {slicer.output_dir}")

        # --- Siguiente paso: Transmitir a DLP LightCrafter ---
        # La parte de "transmitir a DLP LightCrafter" es compleja y depende del modelo específico de LightCrafter.
        # Generalmente, implica usar un SDK o una librería de Python para comunicarse a través de USB.
        # Por ejemplo, para algunos modelos, podrías usar librerías como 'Pycrafter6500' (si es compatible con tu modelo)
        # o la API de TI DLP LightCrafter que requiere controladores específicos.

        print("\nPara transmitir estas imágenes al DLP LightCrafter, necesitarás:")
        print("1. El SDK/API de Texas Instruments para tu modelo específico de DLP LightCrafter.")
        print("2. Una librería de Python (si existe) que envuelva esa API o que se comunique directamente con el dispositivo (ej. via USB/serial).")
        print("3. Programar el LightCrafter para que entre en 'modo de secuencia de patrones' y enviarle estos arrays binarios.")
        print("\nEjemplo conceptual (el código real varía mucho según el modelo):")
        print("""
        # Pseudo-código para cargar al LightCrafter:
        # from pycrafter import LightCrafterController # Librería de ejemplo
        #
        # lc = LightCrafterController(port='COMx') # O dirección IP, o ID USB
        # lc.connect()
        # lc.set_pattern_mode()
        # for i, pattern in enumerate(binary_slices):
        #    lc.load_pattern(pattern, exposure_time=1000) # Tiempo en microsegundos
        # lc.start_pattern_sequence(loop=True)
        #
        # Recuerda que la sincronización con tu mecanismo de pantalla volumétrica es CRÍTICA.
        # A menudo, el LightCrafter puede emitir un pulso de 'trigger out' para cada patrón.
        """)

    except ImportError as e:
        print(f"Error de importación: {e}")
        print("Asegúrate de tener instaladas las librerías: trimesh, pydicom, scikit-image, Pillow.")
        print("Pip install: pip install trimesh pydicom scikit-image Pillow numpy")
        print("También, asegúrate de que 'Shared.classes.ExistsPath' y 'Modeling_3D.config.constantGenerateSTL' sean accesibles.")