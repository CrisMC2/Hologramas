from abc import ABC, abstractmethod

from core.classes.AbsDicomPath import AbsDicomPathsExists, AbsExtractDicomPath, AbsDicomConvertByPath
from core.classes.AbsDicomProcessing import AbsDicomOrder

class AbsDicomExtract(ABC):
    def __init__(self):
        self.dicom_path_exists = AbsDicomPathsExists
        self.extract_dicom_path = AbsExtractDicomPath
        self.dicom_convert_by_path = AbsDicomConvertByPath
        self.dicom_order = AbsDicomOrder
        
    """
    El siguiente método permite extraer archivos dicom a partir de la dirección de 
    un folder o carpeta que contenga todas las direcciones de los dicom.
    
    - El método aprovecha la implementación de diversas clases para su funcionamiento (Todas aquellas definidas en el constructor).
    - El método empieza determinando si la dirección del folder existe
    - El método extrae todas las direcciones (.dcm) en el folder
    - El método convierte todas las direcciones en archivos dicom
    - El método ordena todos los archivos dicom en base al método order_dicom_folder.
    
    - Parámetros:
        - self (AbsDicomExtract)    : Instancia de la clase AbsDicomExtract
        - path_folder (str)         : Dirección del folder que contiene a todos los archivos dicoms
    
    - Retorno:
        - List<dicom>           : Lista de todos los archivos dicom ya extraídos (No procesados mediante houns)
        - None                  : En caso de que algo falle en el código
    
    Para saber detalles adicionales del código revisar la documentación de los métodos y clases usados
    
    """
    def extract_dicoms (self, path_folder: str):
        if self.dicom_path_exists.exists_path(self.dicom_path_exists, path_folder):
            list_paths = self.extract_dicom_path.extract_dicom_paths(path_folder)

            if list_paths:
                list_dicoms = self.dicom_convert_by_path.convert_dicoms_list_path(list_dicoms)   
                list_dicoms = self.dicom_order.order_dicom_folder(list_dicoms)
                return list_dicoms
        
        return None
    
    """
    El siguiente método permite extraer archivos dicom a partir de una lista que contenga todas
    las direcciones de los archivos dicom.
    
    - El método aprovecha la implementación de diversas clases para su funcionamiento (Todas aquellas definidas en el constructor).
    - El método empieza determinando si la dirección del folder existe
    - El método extrae todas las direcciones (.dcm) en el folder
    - El método convierte todas las direcciones en archivos dicom
    - El método ordena todos los archivos dicom en base al método order_dicom_folder.
    
    - Parámetros:
        - self (AbsDicomExtract)    : Instancia de la clase AbsDicomExtract
        - path_folder (str)         : Dirección del folder que contiene a todos los archivos dicoms
    
    - Retorno:
        - List<dicom>           : Lista de todos los archivos dicom ya extraídos (No procesados mediante houns)
        - None                  : En caso de que algo falle en el código
    
    Para saber detalles adicionales del código revisar la documentación de los métodos y clases usados
    
    """
    def extract_dicoms (self, list_paths: list):
        if self.dicom_path_exists.exists_dicom_in_path(list_paths):
            list_dicoms = self.dicom_convert_by_path.convert_dicoms_list_path(list_paths=list_dicoms)
            list_dicoms = self.dicom_order.order_dicom_folder(list_dicoms)

            return list_dicoms
        return None