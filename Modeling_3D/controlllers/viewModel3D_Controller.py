import cv2
import numpy as np

from typing import Union
from functools import partial

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

from Modeling_3D.core.secondThread import ExtraThread
from Modeling_3D.core.GenerateSTL import GenerateSTL
# from Modeling_3D.utils.VideoWidget import VideoWidget
from Modeling_3D.utils.Model3D_Vtk import Model3D_Vtk
from Modeling_3D.utils.WindowInteractor_Vtk import WindowInteractor_Vtk
from Modeling_3D.utils.ConvertFormat import ConvertFormat
from Modeling_3D.Shared.Gesture_Vtk import GestureInteractorStyle
from Modeling_3D.views.viewModel3D import Ui_viewModel3D

from Gestures.main_ import EmitGest;

from Modeling_3D.config import constantGestureMove as consGesMo

class viewModel3D_Controller(Ui_viewModel3D):
    def __init__(self):
        super().__init__()
        # self.setupUi(main_window)
        
        self.__define_objects()
        
    def __define_objects(self):
        # self.video_widget = VideoWidget()
        self.extra_thread_video = ExtraThread()
        self.extra_thread_gesture = ExtraThread()
        # self.emit_gest = EmitGest()
        
        self.gen_stl = GenerateSTL()
        self.convert_format = ConvertFormat()
    
    def execute(self, path_model_stl: str, cap: cv2.VideoCapture):
        self.generate_interactor(data=path_model_stl)
        # self.show_video(cap=cap)  
        # pass
    
    def generate_stl(self, array: list):
        mesh = self.gen_stl.execute(array)
        vtk_mesh = self.convert_format.trimesh_to_vtk(mesh)
        return vtk_mesh
        
    def generate_interactor(self, data: Union[str, list]):
        #Crear el modelo 3D para 
        model_vtk = Model3D_Vtk()
        model_vtk.create_render()
        
        if isinstance(data, list): #En caso de que se haya pasado un arreglo, debemos generar el stl
            data = self.generate_stl(data)
        
        model_vtk.config_scential(data= data)
        model_vtk.config_render(consGesMo.VIEWPORT_RENDER, 
                                consGesMo.BACKGROUND_RENDER, consGesMo.SIZE_RENDER_WINDOW)
        
        # #Creamos la ventana interactiva (Que pueda utilizarse con QT)
        window_interactor = WindowInteractor_Vtk(self.model_Widget)
        render_window = window_interactor.render_window
        render_window.AddRenderer(model_vtk.render)
        
        # #Establecemos el Estilo que tendrá el Render
        self.style_vtk = GestureInteractorStyle(renderer_stl=model_vtk.render, actor=model_vtk.actor,
                                        renderer_cam=None, texture=None)
        
        window_interactor.set_Style(self.style_vtk, model_vtk.render)
        # self.model_Widget.show()
        QApplication.processEvents()
        window_interactor.render()
        # window_interactor.render(model_vtk.render)

        #Necesitamos un nuevo render que pueda tener al método de los gestos
        # gest = EmitGest()
        
        # self.extra_thread_gesture.start_(self.emit_gest.execute, True)
        # self.extra_thread_gesture.connect_signal(self.style_vtk.connect_execute)
        
        return window_interactor
    
    def show_video(self, cap: cv2.VideoCapture):
        
        function_model = partial(self.video_widget.define_components, cap_insert=cap, 
                                            video_label=self.camVideo_Label, 
                                            size_cap=[consGesMo.DEFAULT_CAP_WIDTH, 
                                                        consGesMo.DEFAULT_CAP_HEIGHT])
        
        self.extra_thread_video.start_(func=function_model, func_return=True)
        self.extra_thread_video.connect_signal(self.style_vtk.on_signal)
        self.extra_thread_video.connect_signal(self.__complete_information)
        
        self.video_widget.start_timer()
    
    def __complete_information(self):
        if hasattr(self.video_widget, "predict") and hasattr(self.video_widget, "value_predict"):
            self.label_prediction_info.setText(self.video_widget.predict)
            self.label_security_info.setText(self.video_widget.value_predict)
    
    def _stop_working(self):
        self.extra_thread_video.stop()
        self.extra_thread_gesture.stop()