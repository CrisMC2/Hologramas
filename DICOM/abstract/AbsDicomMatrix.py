import numpy as np

from abc import ABC, abstractmethod

class AbsDicomMatrix(ABC):
    def generate_matrix (self, lista_dicoms: list, hounsmin=-200, hounsmax=200):
        lista_dicoms = list(map(lambda dc: self.processing_dicom(dc, hounsmin, hounsmax), lista_dicoms))
        
        #Shape => (profundidad, filas, columnas)
        lista_dicoms = np.array(lista_dicoms)
        return lista_dicoms    