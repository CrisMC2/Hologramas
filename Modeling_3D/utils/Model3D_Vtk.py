import vtk

class Model3D_Vtk():
    def __init__(self):
        self.create_scential()
    
    def create_scential(self):
        self.reader = vtk.vtkSTLReader()
        self.mapper = vtk.vtkPolyDataMapper()
        self.actor = vtk.vtkActor()
    """
    El mapper es responsable de convertir la información 3D del modelo (proporcionada por el lector STL)
        en datos que pueden ser utilizados por VTK para renderizar la geometría del modelo
        
    El actor es un objeto que tiene el modelo 3D mapeado (con los datos del mapper) y lo puede agregar
        a un renderizador. Es esencialmente el "objeto" visual que aparece en la escena 3D.   
    """
    def create_render(self, render_window: bool = False):
        self.render = vtk.vtkRenderer()
        self.render.AddActor(self.actor)
        
        if render_window:
            self.render_window = vtk.vtkRenderWindow()
            self.render_window.AddRenderer(self.render)
        
    def config_scential(self, path:str):
        self.reader.SetFileName(path)
        self.mapper.SetInputConnection(self.reader.GetOutputPort())
        self.actor.SetMapper(self.mapper)
    
    def config_render(self, viewport_render: list[float, float, float, float], background: list[float, float, float],
                      size_render_window: list[int, int]=None):
        
        self.render.SetViewport(viewport_render[0], viewport_render[1], viewport_render[2], viewport_render[3])
        self.render.SetBackground(background[0], background[1], background[2])
        
        if hasattr(self, "self.render_window"):
            self.render_window.SetSize(size_render_window[0], size_render_window[1])
    
    def addRender(self, render: vtk.vtkRenderWindow):
        self.render_window.AddRenderer(render)
    
    
    
    
            
#     # Función principal para cargar el modelo 3D, configurar la ventana y manejar la interacción con la cámara
# def lector_vtk(path: str):
#         # STL
#         reader = vtk.vtkSTLReader()
#         # reader.SetFileName("E:\\PruebasRadiograficas-STL\\RAMIREZ_ACAPANA_TEODORO.stl")
#         reader.SetFileName(path)
#         mapper = vtk.vtkPolyDataMapper()
#         mapper.SetInputConnection(reader.GetOutputPort())
#         actor = vtk.vtkActor()
#         actor.SetMapper(mapper)
        

#         # Crear una ventana para renderizar
#         renderWindow = vtk.vtkRenderWindow()
#         renderWindow.SetSize(1280, 720)
#         # La ventana de renderizado es donde se visualizará todo lo que se renderice.

#         # Crear un renderizador para la cámara
#         renderer_cam = vtk.vtkRenderer()
#         renderer_cam.SetViewport(0.0, 0.0, 0.3, 1.0)
#         renderer_cam.SetBackground(0.2, 0.2, 0.2)
        
        
        
#         # Crear un plano con textura
#         planeSource = vtk.vtkPlaneSource()
#         planeSource.SetOrigin(1.0, 1.0, 0.0)
#         planeSource.SetPoint1(0.0, 1.0, 0.0)
#         planeSource.SetPoint2(1.0, 0.0, 0.0)
#         planeSource.Update()

#         texture = vtk.vtkTexture()
#         texture.InterpolateOn()
        
#         # Crear un actor para el plano de textura
#         mapper_plane = vtk.vtkPolyDataMapper()
#         mapper_plane.SetInputConnection(planeSource.GetOutputPort()) 
#         # El mapper del plano convierte la geometría generada por el `planeSource` en algo que puede ser visualizado
#         actor_plane = vtk.vtkActor()
#         actor_plane.SetMapper(mapper_plane)  # Asocia el mapper del plano al actor del plano
#         actor_plane.SetTexture(texture)

#         renderer_cam.AddActor(actor_plane)  # Agregar el actor del modelo STL al renderizador STL

#         # Crear un renderizador para el modelo STL
#         renderer_stl = vtk.vtkRenderer()
#         renderer_stl.SetViewport(0.3, 0.0, 1.0, 1.0)
#         renderer_stl.SetBackground(1.0, 1.0, 1.0)
#         renderer_stl.AddActor(actor)

#         renderWindow.AddRenderer(renderer_cam)
#         renderWindow.AddRenderer(renderer_stl)
        
#         # Crear el interactor para la ventana de renderizado
#         renderWindowInteractor = vtk.vtkRenderWindowInteractor()
#         renderWindowInteractor.SetRenderWindow(renderWindow)
        
#         # Establecer el estilo de interacción personalizado con los gestos
#         style = GestureInteractorStyle(renderer_stl, actor, renderer_cam, texture)
#         style.SetDefaultRenderer(renderer_stl)
#         renderWindowInteractor.SetInteractorStyle(style)
        
#         # Inicializar y comenzar el bucle de renderizado
#         renderWindow.Render()
#         renderWindowInteractor.Initialize()
#         renderWindowInteractor.CreateRepeatingTimer(1)
#         renderWindowInteractor.Start()