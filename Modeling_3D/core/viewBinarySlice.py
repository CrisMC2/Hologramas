import os
import numpy as np
import pyvista as pv
from PIL import Image # Asumiendo que tus slices se generaron con PIL

# --- PASO 1: Simular la generación de binary_slices (reemplaza esto con tu código real) ---
# Si no tienes tu código de slicing a mano o quieres probar rápido:
def create_dummy_binary_slices(num_slices=50, res_xy=(64, 64)):
    dummy_slices = []
    # Crea un "cilindro" binario simple como ejemplo
    center_x, center_y = res_xy[0] // 2, res_xy[1] // 2
    radius_base = res_xy[0] // 3
    for i in range(num_slices):
        img_slice = np.zeros(res_xy, dtype=np.uint8)
        # Radio que varía con la altura para simular una forma más compleja
        current_radius = radius_base * (1 - abs((i - num_slices/2) / (num_slices/2))) 
        for x in range(res_xy[0]):
            for y in range(res_xy[1]):
                if (x - center_x)**2 + (y - center_y)**2 < current_radius**2:
                    img_slice[y, x] = 255 # Píxel blanco
        dummy_slices.append(img_slice)
    return dummy_slices

# Si ya generaste tus slices con el script anterior:
# Asegúrate de que 'sliced_patterns' sea la carpeta donde se guardaron
# binary_slices = []
# for i in range(num_slices_to_project): # Usa el mismo num_slices que usaste antes
#    slice_path = os.path.join("sliced_patterns", f"slice_{i:04d}.png")
#    img = Image.open(slice_path).convert('L') # Abrir en escala de grises
#    binary_slices.append(np.array(img))

def view_binary_slices(num_slices, folder: str):
    # Ejemplo usando el dummy_slices para demostración
    # binary_slices = create_dummy_binary_slices(num_slices=100, res_xy=(64, 64))
    # binary_slices=mesh
    binary_slices = []
    for i in range(num_slices): # Usa el mismo num_slices que usaste antes
        slice_path = os.path.join(folder, f"voxel_slice_{i:04d}.jpg")
        print(slice_path, end="\n\n")
        img = Image.open(slice_path).convert('L') # Abrir en escala de grises
        binary_slices.append(np.array(img))
    # --- FIN de la simulación de binary_slices ---

    # --- PASO 2: Apilar las imágenes binarias para formar un volumen 3D ---
    # Asegúrate de que todas las imágenes tengan el mismo tamaño
    if not binary_slices:
            print("No hay slices binarios para visualizar.")
            exit()

        # Convierte la lista de arrays 2D a un solo array 3D
        # Asegúrate de que el dtype sea apropiado para Marching Cubes (ej. int8, float)
    volume_data = np.stack(binary_slices).astype(np.int8) # (num_slices, height, width)
    print(volume_data)
        # Si necesitas reordenar las dimensiones (PyVista/VTK a menudo prefiere (width, height, depth)):
        # volume_data = np.transpose(volume_data, (2, 1, 0)) # (width, height, depth)

    print(f"Volumen 3D binario creado con forma: {volume_data.shape}")

        # --- PASO 3: Visualizar el volumen binario como una isosuperficie ---

        # Crear un objeto de datos de imagen de PyVista
        # PyVista usa la convención (X, Y, Z) para dimensiones
        # Si tu stack es (Z, Y, X), entonces necesitas pasarlo como (Z, Y, X)
        # Y luego, si lo necesitas para Marching Cubes, quizás transponerlo
        # Marching cubes opera en el 'campo escalar', aquí 0s y 255s.
        # Queremos la superficie donde el valor es '1' o '255'
    surface = pv.wrap(volume_data).contour(128) # Umbral en el medio para 0s/255s
    print("Primer avance")
        # Crear un ploter de PyVista
    p = pv.Plotter()
    # Añadir la superficie al ploter
    p.add_mesh(surface, color='lightblue', show_edges=False, opacity=0.8)
    print("Segundo avance")

        # --- PASO 4 (Opcional): Añadir contexto visual ---
        # Puedes añadir un cubo transparente para representar el volumen de proyección del DLP
        # La extensión del cubo debe coincidir con las dimensiones de tu volumen de datos
    bounds = surface.bounds # Obtiene los límites [xmin, xmax, ymin, ymax, zmin, zmax] de la superficie
        # Crea un cubo usando esos límites
    bounding_box = pv.Cube(bounds=bounds).extract_all_edges()
    p.add_mesh(bounding_box, color='gray', style='wireframe', opacity=0.2, line_width=1)
    print("Tercer avance")

        # Añadir un plano inferior simulando una base (opcional)
        # p.add_plane(normal=[0,0,1], i_size=bounds[1]-bounds[0], j_size=bounds[3]-bounds[2], center=[(bounds[0]+bounds[1])/2, (bounds[2]+bounds[3])/2, bounds[4]], color='lightgray', opacity=0.3)


        # Configurar cámara y título
    p.camera_position = 'iso' # Vista isométrica
    p.add_title("Simulación de Proyección Volumétrica (DLP LightCrafter)")

        # Mostrar la visualización
    p.show()