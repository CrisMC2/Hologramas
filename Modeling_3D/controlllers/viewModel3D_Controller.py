import cv2

from PyQt5.QtWidgets import QWidget, QMainWindow

from Modeling_3D.utils.VideoWidget import VideoWidget
from Modeling_3D.utils.Model3D_Vtk import Model3D_Vtk
from Modeling_3D.utils.WindowInteractor_Vtk import WindowInteractor_Vtk
from Modeling_3D.Shared.Gesture_Vtk import GestureInteractorStyle
from Modeling_3D.views.viewModel3D import Ui_viewModel3D

from Modeling_3D.config import constantGestureMove as consGesMo

class viewModel3D_Controller(Ui_viewModel3D):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        # self.setupUi(main_window)
        
        self.__define_objects()
        
    def __define_objects(self):
        self.video_widget = VideoWidget()
    
    def generate_interactor(self, path: str):
        #Crear el modelo 3D para 
        model_vtk = Model3D_Vtk()
        model_vtk.create_render()
        model_vtk.config_scential(path= path)
        model_vtk.config_render(consGesMo.VIEWPORT_RENDER, 
                                consGesMo.BACKGROUND_RENDER, consGesMo.SIZE_RENDER_WINDOW)
        
        #Creamos la ventana interactiva (Que pueda utilizarse con QT)
        window_interactor = WindowInteractor_Vtk(self.model_Widget)
        render_window = window_interactor.render_window
        render_window.AddRenderer(model_vtk.render)
        
        #Establecemos el Estilo que tendrá el Render
        self.style_vtk = GestureInteractorStyle(renderer_stl=model_vtk.render, actor=model_vtk.actor,
                                        renderer_cam=None, texture=None)
        
        window_interactor.set_Style(self.style_vtk, model_vtk.render)
        # window_interactor.show()
        window_interactor.render()

        ###Necesitamos un nuevo render que pueda tener al método de los gestos
        # gest = EmitGest()
        # thread = ExtraThread()
        
        # thread.start_(gest.execute, True)
        # thread.connect_signal(style_vtk.connect_execute)
        
        # return window_interactor
    
    def show_video(self, cap: cv2.VideoCapture):
        self.video_widget.define_components(cap_insert=cap, 
                                            video_label=self.camVideo_Label, 
                                            size_cap=[consGesMo.DEFAULT_CAP_WIDTH, 
                                                      consGesMo.DEFAULT_CAP_HEIGHT])   
        self.style_vtk.connect_execute(self.video_widget.signal.obj_signal)
        
    