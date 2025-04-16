import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from typing import Union

from core.classes.DicomPath import DicomPathsExists, ExtractDicomPath, DicomConvertByPath
from core.classes.DicomProcessing import DicomOrder

class DicomExtract():
    def __init__(self):
        self.dicom_path_exists = DicomPathsExists()
        self.extract_dicom_path = ExtractDicomPath()
        self.dicom_convert_by_path = DicomConvertByPath()
        self.dicom_order = DicomOrder()

    @type.overload
    def extract_dicoms(self, path_folder: str) -> None | list: ...
    
    @type.overload
    def extract_dicoms(self, list_path: list) -> None | list: ...
    
    
    
    def extract_dicoms(self, folder: Union[str, list]) -> None | list:
        list_paths = list()
        if isinstance(folder, str):
            if self.dicom_path_exists.exists_path(folder, False): #Agregamos el path e impedimos que en caso de no existir, se cree.
                list_paths = self.extract_dicom_path.extract_dicom_paths(folder)
                
        elif isinstance(folder, list):
            if self.dicom_path_exists.exists_dicom_in_path(folder): #verificamos que haya al menos un archivo dicom en la lista
                list_paths = folder
        
        else: #En caso de no tener una instancia de un string o una lista, lanzamos un error.
            raise TypeError("El tipo de dato que intentas ingresar para el parámetro folder no es válido, intenta con: String | list")

        
        if list_paths:
            list_dicoms = self.dicom_convert_by_path.convert_dicoms_list_path(list_paths=list_paths)
            list_dicoms = self.dicom_order.order_dicom_folder(list_dicoms) #Puede que sea necesario poner True
            return list_dicoms
                
        
    
    def extract_dicoms_by_folder (self, path_folder: str) -> list | None:
        if self.dicom_path_exists.exists_path(self.dicom_path_exists, path_folder):
            list_paths = self.extract_dicom_path.extract_dicom_paths(path_folder)

            if list_paths:
                list_dicoms = self.dicom_convert_by_path.convert_dicoms_list_path(list_paths)   
                list_dicoms = self.dicom_order.order_dicom_folder(list_dicoms)
                return list_dicoms
        
        return None
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
   
    def extract_dicoms_by_list (self, list_paths: list):
        if self.dicom_path_exists.exists_dicom_in_path(list_paths):
            list_dicoms = self.dicom_convert_by_path.convert_dicoms_list_path(list_paths=list_dicoms)
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