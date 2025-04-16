import os
import sys

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

import numpy as np

from core.classes.DicomView import ViewAxial, ViewCoronal, ViewSagittal  

class DefineViewDicom():
    def __init__(self):
        self.obj_axial = ViewAxial()
        self.obj_saggital = ViewSagittal()
        self.obj_coronal = ViewCoronal()
        
    def return_view(self, matrix_3d: np.array[int, int, int], element_matrix: int, view: str = "Axial View"):
        img_array = np.array()
        
        if view == "Axial View":
            img_array = self.obj_axial.create_view(matrix_3d, element_matrix)
            
        elif view == "Saggital View":
            img_array = self.obj_saggital.create_view(matrix_3d, element_matrix)
        
        elif view == "Coronal View":
            img_array = self.obj_coronal.create_view(matrix_3d, element_matrix)
            
        else:
            raise TypeError("El tipo de vista ingresada no es correcta, intenta con: Axial View | Saggital View | Coronal View")
        
        return img_array