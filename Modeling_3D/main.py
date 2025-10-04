import cv2
import sys
import numpy as np

from typing import Union
from PyQt5.QtWidgets import QApplication, QMainWindow

from Modeling_3D.controlllers.viewModel3D_Controller import viewModel3D_Controller
from Modeling_3D.core.GenerateSTL import GenerateSTL

def execute(data: Union[str, np.array]):
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = viewModel3D_Controller()
    
    ui.setupUi(main_window)
    main_window.show()

    cap = cv2.VideoCapture(0)
    
    ui.execute(path_model_stl=data, 
               cap=cap)

    
    sys.exit(app.exec_())