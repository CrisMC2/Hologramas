import vtk
# import numpy as np

# from typing import Union
# from PyQt5.QtWidgets import QApplication, QMainWindow

# from Modeling_3D.controlllers.viewModel3D_Controller import viewModel3D_Controller
from Modeling_3D.core.GenerateSTL import GenerateSTL
from Modeling_3D.utils.ConvertFormat import ConvertFormat
from Modeling_3D.core.BinarySlice import SlicerForLightCrafter
from Modeling_3D.core.viewBinarySlice import view_binary_slices

def mostrar_malla_vtk(polydata, ruta_archivo_stl, filename):
    """
    Muestra un vtkPolyData (malla) en una ventana VTK.

    Args:
        polydata (vtk.vtkPolyData): El objeto vtkPolyData que representa la malla.
    """
    print("Iniciando visualización")

    reader = vtk.vtkSTLReader()
    reader.SetFileName(ruta_archivo_stl)
    reader.Update() 
    # 1. Crear un Mapeador (Mapper)
    # El mapeador toma los datos de la malla y los prepara para la visualización.
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    # mapper.SetInputData(polydata) # O mapper.SetInputConnection(source.GetOutputPort()) si viene de un filtro

    # 2. Crear un Actor (Actor)
    # El actor es la representación visual de la malla en la escena.
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Opcional: Configurar propiedades del actor
    # actor.GetProperty().SetColor(1.0, 0.0, 0.0)  # Rojo
    # actor.GetProperty().SetRepresentationToWireframe() # Mostrar como alámbrico
    # actor.GetProperty().SetOpacity(0.5) # Transparencia

    # 3. Crear un Renderizador (Renderer)
    # El renderizador es el "ojo" que ve la escena.
    print("Configurando Render")

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.2, 0.2, 0.2) # Color de fondo (oscuro azulado)

    # 4. Crear una Ventana de Renderizado (Render Window)
    # La ventana donde se mostrará la escena.
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)
    render_window.SetSize(800, 600) # Tamaño de la ventana
    render_window.SetWindowName("Visualización de Malla VTK - "+filename)

    print("Renderizando ventana interactiva")
    # 5. Crear un Interactor (Interactor)
    # Permite la interacción del usuario con la escena (rotar, zoom, panear).
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(render_window)

    # Inicializar el interactor y comenzar el bucle de eventos
    print("Mostrando")

    render_window.Render()
    interactor.Initialize()
    interactor.Start()
    print("Inicio")


if __name__ == "__main__":
    stl = r"Modeling_3D\resources\Prueba Marching-Cubes-300HU-2.stl"
    filename = "Marching-Cubes-300HU"
    dicom_folder = r"Modeling_3D\resources\CT Cuerpo 1.0"
    output_folder = r"Modeling_3D\resources"
    stl_filename = "Prueba Marching-Cubes-300HU-2"

    gen = GenerateSTL()
    convert = ConvertFormat()
    

    print("Iniciando conversión a stl\n\n")
    mesh = gen.execute(dicom_folder
                       , output_folder, stl_filename)
    mesh = convert.trimesh_to_vtk(mesh)

    print("Conversión a stl Terminada\n\n")

    mostrar_malla_vtk("", stl, filename)


    # #============= BINARIZAR ================
    # print("Iniciando binarización\n\n")
    # bin = SlicerForLightCrafter(mesh)
    # # # binary_mesh = bin.slice_mesh(400)
    # binary_mesh = bin.binarize_mesh_by_surface_voxelization(1)
    # print("Binarización terminada\n\n")

    # print("Iniciando visualización\n\n")

    # view_binary_slices(490, "voxel_slices_skeleton_1")

    # print("Visualización terminada\n\n")