from abc import ABC, abstractmethod
import numpy as np

class AbsDicomView(ABC):
    
    @abstractmethod
    def create_view(self, matriz_dicom: np.array, i: int):
        pass
    
    """
    El método create_view permite crear una vista de una tomografía computarizada (Axial, Coronal y Sagital)
    a partir de una matriz rellena de arrays dicom.
    
    - Parámetros:
        - self (AbsDicomView)           : Instancia de la clase AbsDicomView
        - array_dicoms (numpy.array)    : Arreglo tridimensional que contiene todos los arreglos de cada folder dicom
        - i (int)                       : Iterador que determinará que parte del arreglo se desea obtener
        
    - Retorno:
        - Array_dicom[i,:,:]    : Arreglo tridimensional ya segmentado
    """

    @abstractmethod
    def define_aspect(self):
        pass