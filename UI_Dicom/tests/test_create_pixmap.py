import os
import sys

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

import matplotlib.pyplot as plt
import numpy as np

from UI_Dicom.core.classes.DicomRead import AbsDicomRead
from core.classes.DicomMatrix import DicomMatrix
from core.classes.DicomProcessing import DicomProccessing
from UI_Dicom.utils.Pixmap import Pixmap

def create_matrix(path: str, show: bool, return_: bool) -> None:    
    dicom_read = AbsDicomRead()
    dicom_matrix = DicomMatrix()
    
    dicom = dicom_read.read_dicom(path)
    matriz = dicom_matrix.generate_matrix([dicom])
    
    if show:
        plt.imshow(matriz[0], cmap="gray")
        plt.show()
        
    if return_:
        return matriz
    
def create_pixmap(path: str):
    pixmap = Pixmap()
    
    matriz = create_matrix(path, False, True)
    
    pixmap = pixmap.create_pixmap(matriz)
    
    plt.imshow(pixmap)
    plt.show()

if __name__ == "__main__":
    path = "E:\\UNCP\\SEMILLEROS\\PROYECTO\\PRUEBAS\\1348 RAMIREZ ACAPANA TEODORO VICTOR\\34303\\CT Cuerpo 1.0\\CT000000.dcm"
    # create_matrix(path, True, False)
    create_pixmap(path)