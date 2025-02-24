import numpy as np

from abc import ABC, abstractmethod

from core.classes.AbsDicomProcessing import AbsDicomProccessing
class AbsDicomMatrix(ABC, AbsDicomProccessing):
    def generate_matrix (self, lista_dicoms: list, hounsmin=-200, hounsmax=200):
        lista_dicoms = list(map(lambda dc: self.processing_dicom(dc, hounsmin, hounsmax), lista_dicoms)) #Si así no funciona cambiar el "list()" por "[]"
        
        #Shape => (profundidad, filas, columnas)
        lista_dicoms = np.array(lista_dicoms)
        return lista_dicoms    