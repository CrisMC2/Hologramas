import cv2
import sys
import numpy as np

from typing import Union
from PyQt5.QtWidgets import QApplication, QMainWindow

from Modeling_3D.controlllers.viewModel3D_Controller import viewModel3D_Controller
from Modeling_3D.core.GenerateSTL import GenerateSTL

class Execute_Modeling3D:
    def __init__(self):
        self.views = []
    
    def execute(self, data: Union[str, list]):
        app = QApplication.instance() # Utilizamos la instancia ya existente
        
        if app is None:
            print("Error: La aplicación no está ejecutando")
            return
        
        main_window = QMainWindow()
        self.ui = viewModel3D_Controller()
        
        self.ui.setupUi(main_window)
        
        self.views.append(main_window)
        
        main_window.show()

        cap = cv2.VideoCapture(1)
        
        self.ui.execute(path_model_stl=data,
                cap=cap)
        
        # En caso el main_window sea cerrado
        main_window.destroyed.connect(self.close_window)

    def close_window(self):
        self.ui._stop_working