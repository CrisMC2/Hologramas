import numpy as np

from DICOM.core.classes.DicomProcessing import AbsDicomProccessing

class DicomMatrix(AbsDicomProccessing):
    def generate_matrix (self, lista_dicoms: list, hounsmin=-200, hounsmax=200):
        lista_dicoms = list(map(lambda dc: self.processing_dicom(dc, hounsmin, hounsmax), lista_dicoms)) #Si así no funciona cambiar el "list()" por "[]"
        
        #Shape => (profundidad, filas, columnas)
        lista_dicoms = np.array(lista_dicoms)
        return lista_dicoms    