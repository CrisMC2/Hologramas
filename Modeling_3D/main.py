from Modeling_3D.config import constantGestureMove as consGesMo
from Modeling_3D.core.secondThread import ExtraThread

from Modeling_3D.Shared.Gesture_Vtk import GestureInteractorStyle
from Modeling_3D.utils.Model3D_Vtk import Model3D_Vtk
from Modeling_3D.utils.WindowInteractor_Vtk import WindowInteractor_Vtk

from Gestures.main_ import EmitGest

def execute(path: str):
    #Crear el modelo 3D para 
    model_vtk = Model3D_Vtk()
    model_vtk.create_render()
    model_vtk.config_scential(path= path)
    model_vtk.config_render(consGesMo.VIEWPORT_RENDER, 
                            consGesMo.BACKGROUND_RENDER, consGesMo.SIZE_RENDER_WINDOW)
    
    #Creamos la ventana interactiva (Que pueda utilizarse con QT)
    window_interactor = WindowInteractor_Vtk()
    render_window = window_interactor.render_window

    #Establecemos el Estilo que tendrá el Render
    style_vtk = GestureInteractorStyle(renderer_stl=model_vtk.render, actor=model_vtk.actor,
                                       renderer_cam=None, texture=None)
    
    window_interactor.set_Style(style_vtk, model_vtk.render)
    window_interactor.show()
    window_interactor.render()

    #Añadimos los Render al WindowInteractor
    render_window.AddRenderer(model_vtk.render)
    ###Necesitamos un nuevo render que pueda tener al método de los gestos
    # gest = EmitGest()
    # thread = ExtraThread()
    
    # thread.start_(gest.execute, True)
    # thread.connect_signal(style_vtk.connect_execute)
    
    return window_interactor