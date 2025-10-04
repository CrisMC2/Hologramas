import numpy as np
import matplotlib.pyplot as plt #Para arreglar errores

from UI_Dicom.core.classes.DicomView import AxialView, CoronalView, SagittalView  
from UI_Dicom.config import constantViewDICOM as consVDcm 

class DefineViewDicom():
    def __init__(self):
        self.obj_axial = AxialView()
        self.obj_saggital = SagittalView()
        self.obj_coronal = CoronalView()
        
    def return_view(self, matrix_3d: np.array, iterator_matrix: int, view: str) -> np.array:
        # img_array = np.zeros(1)
        
        if view == consVDcm.VIEWS_DICOM[0]:
            img_array = self.obj_axial.create_view(matrix_3d, iterator_matrix)

        elif view == consVDcm.VIEWS_DICOM[1]:
            img_array = self.obj_saggital.create_view(matrix_3d, iterator_matrix)

        elif view == consVDcm.VIEWS_DICOM[2]:
            img_array = self.obj_coronal.create_view(matrix_3d, iterator_matrix)

        else:
            raise TypeError("El tipo de vista ingresada no es correcta, intenta con: Axial View | Saggital View | Coronal View")
        
        return img_array

    def return_size_view(self, matrix_3d: np.array, view: str, edit_get: int = None) -> int:
        size_view = 0

        if view == consVDcm.VIEWS_DICOM[0]:
            size_view = matrix_3d.shape[0]

        elif view == consVDcm.VIEWS_DICOM[1]:
            size_view = matrix_3d.shape[1]
            
        elif view == consVDcm.VIEWS_DICOM[2]:
            size_view = matrix_3d.shape[2]

        else:
            raise TypeError("El tipo de vista ingresada no es correcta, intenta con: Axial View | Saggital View | Coronal View")
        
        if edit_get:
            return size_view + edit_get
            
        return size_view
    
    """
    El método return_size_view de la clase DefineViewDicom.
    """