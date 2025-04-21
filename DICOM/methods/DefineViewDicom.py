import numpy as np

from core.classes.DicomView import ViewAxial, ViewCoronal, ViewSagittal  
from config import constantViewDICOM as consVDcm 

class DefineViewDicom():
    def __init__(self):
        self.obj_axial = ViewAxial()
        self.obj_saggital = ViewSagittal()
        self.obj_coronal = ViewCoronal()
        
    def return_view(self, matrix_3d: np.array, element_matrix: int, view: str):
        img_array = np.array()
        
        if view == consVDcm.VIEWSDICOM[0]:
            img_array = self.obj_axial.create_view(matrix_3d, element_matrix)
            
        elif view == consVDcm.VIEWSDICOM[1]:
            img_array = self.obj_saggital.create_view(matrix_3d, element_matrix)
        
        elif view == consVDcm.VIEWSDICOM[2]:
            img_array = self.obj_coronal.create_view(matrix_3d, element_matrix)
            
        else:
            raise TypeError("El tipo de vista ingresada no es correcta, intenta con: Axial View | Saggital View | Coronal View")
        
        return img_array

    def return_size_view(self, matrix_3d: np.array, view: str):
        size_view = int

        if view == consVDcm.VIEWSDICOM[0]:
            size_view = matrix_3d.shape[0]

        elif view == consVDcm.VIEWSDICOM[1]:
            size_view = matrix_3d.shape[1]
            
        elif view == consVDcm.VIEWSDICOM[2]:
            size_view = matrix_3d.shape[2]

        else:
            raise TypeError("El tipo de vista ingresada no es correcta, intenta con: Axial View | Saggital View | Coronal View")
        
        return size_view