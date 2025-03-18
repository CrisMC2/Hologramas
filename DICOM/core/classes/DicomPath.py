#Importamos clases
import os
import sys

#Importamos parte de las clases
from abc import ABC, abstractmethod
from glob import glob


_append = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(_append)

#Importamos clases propias del proyecto
from DICOM.core.abstracts.AbsDicomRead import AbsDicomRead
from DICOM.abstracts.classes.AbsPath        import AbsPath 

class AbsDicomPathsExists(AbsPath):
    
    #Leer la documentación proveniente del AbsPath
    def exists_path(self, path: str, create: bool):
        try:
            if os.path.exists(path):
                return True
            elif create:
                os.makedirs(path)
                return True
            else:
                return False
        except:
            print("La ubicación proporcionada no pudo ser leída.")
    
    
    """
    El siguiente método permite verificar si al menos existe un archivo DICOM (".dcm") 
    en un grupo de direcciones especificadas.
    
    Parámetros:
        - self (AbsDicomPathsExists)    : Instancia de la clase AbsDicomPathsExists
        - path_folder (List<String>)    : Dirección del folder en el que se encuentran los archivos DICOM
    
    Retorno:
        - Bool          : True si al menos una dirección cumple con tener la extensión ".dcm"
                          False si ninguna dirección cumple con la condición
    
    """
    def exists_dicom_in_path(self, path_folder: list):
        if all(self.exists_path(path, False) for path in path_folder): #Primero verificamos si todas las direcciones existen
            return any(os.path.splitext(file)[1] == '.dcm' for file in path_folder) # "any" retornar True si al menos uno de los archivos cumplen con la condición 

#TEMPLATE
class AbsExtractDicomPath(ABC):
    
    """
    El método extrae todos los archivos con extensión '.dcm' desde una ruta especificada.
    
    
    Parámetros:
        - self (DicomExtract_)      : Instancia de la clase AbsExtractDicomPath_
        - path_folder (String)      : Dirección del folder donde se encuentran los archivos DICOM
        
    Retonar:
        - list_ (Lista)             : Todos las rutas de archivos DICOM que fueron encontradas.
    
    Excepción:
        - NotFoundException         : Si la dirección no puede ser leída.
        
    """
    def extract_dicom_paths(self, path_folder: str):
        try:
            list_ = glob(os.path.join(path_folder,"*.dcm"))
            if not list_:
                print(f"La dirección especificada {path_folder} no contiene ningún archivo DICOM.")

            return list_
        except:
            print(f"No se pudo extraer los archivos desde la dirección especificada {path_folder}.")
            return None
     
class AbsDicomConvertByPath (ABC):
    """
    Constructor de la clase AbsDicomConvertByPath.
    
    - Genera una instancia de la clase abstracta AbsDicomRead_
    """
    def __init__(self):
        self.read = AbsDicomRead()
        
    """
    El método tiene como función convertir una lista de direcciones (paths) en archivos dicom.
    
    - El método permite leer múltiples direcciones (paths) a partir de una lista.
    - La lista de direcciones (paths) será filtrada a solo los elementos con extensión ".dcm"
    - Todos aquellos elementos filtrados serán convertidos en archivo dicom.
    - La librería usada es Pydicom
    
    Parámetros:
        - self  (DicomConvertByPath)   : Instancia de la clase AbsDicomConvertByPath.
        - list_paths (List<String>) : Lista de direcciones de archivos dicom.
        
    Retornar:
        - list_dicoms (List<dicom>) : Lista de los archivos dicom que fueron procesados a partir de las direcciones.
    
    """    
    def convert_dicoms_list_path(self, list_paths: list[str]):
        # list_dicoms = list(map(lambda file : file if os.path.splitext(file)[1] == '.dcm' else None), list_paths)
        # list_dicoms = list(file for file in list_dicoms if file is not None)    
        
        list_dicoms = list(file for file in list_paths if os.path.splitext(file)[1] == ".dcm") #Si falla cambia la "list()"" por "[]"
        
        if (list_dicoms):
            list_dicoms = [self.read.read_dicom(file_dicom) for file_dicom in list_dicoms] #Convertimos cada elemento en un archivo dicom
        else:
            print(f"Ninguna dirección en la lista de direcciones: \n\n{list_paths}\n\n Cumple con la extensión \"dicom\"")
           
        return list_dicoms