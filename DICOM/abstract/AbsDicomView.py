from abc import ABC, abstractmethod
import pydicom as dicom
import numpy

from abstract.AbsDicomProcessing import AbsDicomProccessing, AbsDicomOrder
from abstract.AbsDicomPath import AbsDicomPathsExists, AbsExtractDicomPath, AbsDicomConvertByPath

class AbsDicomView(AbsExtractDicomPath, AbsDicomProccessing, AbsDicomOrder, AbsDicomPathsExists, AbsDicomConvertByPath):
    @abstractmethod
    def create_view(self, matriz_dicom: numpy, i: int):
        pass

    @abstractmethod
    def define_aspect(self):
        pass
    
    """
    Este método permite extraer una serie de direcciones con la extensión ".dcm" 
    a partir de una dirección especifica (folder).
    
    - El método verifica que la dirección primeramente exista
    - El método extrae las direcciones de los dicom
    - El método convierte en instancias de la pydicom a todas las direcciones dicom
    - Por último se ordena la lista de dicoms
    
    Parámetros:
        - path_folder (str)            : Dirección del folder que contiene a los archivos dicom
    
    Retorno:
        - lista_dicoms (List<pydicom>) : Lista que contiene a los archivos pydicom
    """
    def extract_multi_dicoms (self, path_folder: str):
        if AbsDicomPathsExists.exists_path(AbsDicomPathsExists, path_folder):
            list_dicoms = AbsExtractDicomPath.extract_path_dicoms(path_folder)

            if list_dicoms:
                list_dicoms = self.convert_dicoms_list_path(list_dicoms)   
                list_dicoms = self.order_dicom(list_dicoms)
                return list_dicoms