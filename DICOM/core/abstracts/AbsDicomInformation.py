from abc import ABC, abstractmethod
import pydicom as dicom

from AbsDicomRead import AbsDicomRead

#Toda la información de DICOM
class AbsDicomInformation (ABC):
    """
    Constructor de la clase AbsDicomInformation
    
    - Genera una instancia de la clase AbsDicomRead()
    """
    def __init__(self):
        self.read= AbsDicomRead()
    
    """
    El método get_information permite obtener información de un archivo Pydicom.
    
    - A partir de valores booleanos podemos obtener los datos que necesitamos o requerimos.
    
    Parámetros:
        - self (AbsDicomInformation)        : Instancia de la claseAbsDicomInformation
        
    Información de Instancia:
        - List<bool>            : Se tiene pensado que el método tenga una serie de valores booleanos
                                    los cuales dependiendo de la instancia devuelvan uno u otro valor.
    """
    @abstractmethod
    def get_information(self, *args, **kwargs) -> dict:
        pass
    
    
    """
    El método set_information permite setear (cambiar, modificar) información de un archivo Pydicom.
    
    - A partir de valores booleanos podemos editar los datos que necesitamos o requerimos.
    
    Parámetros:
        - self (AbsDicomInformation)        : Instancia de la claseAbsDicomInformation
        
    Información de Instancia:
        - List<bool>            : Se tiene pensado que el método tenga una serie de valores booleanos
                                    los cuales dependiendo de la instancia  uno u otro valor.
    """
    @abstractmethod
    def set_information(self, *args, **kwargs):
        pass

class AbsDicomAnonimize(ABC):
    @abstractmethod
    def anonymize_dicom(self, dc: dicom, PatientName="Desconocido", PatientID="Nan", PatientBirthDate="Nan", PatientSex="Nan", 
                        StudyDate="Nan", StudyTime="Nan", InstitutionName="Nan", InstitutionAdress="Nan"):
        pass   
    
    """
    El siguiente método permite "anonimizar un DICOM".
    
    Esto incumbe cambiar datos delicados y privados del paciente que puedan comprometer su integridad.        
    
    Parámetros:
        - self (AbsDicomAnonimize)      : Instancia de la clase AbsDicomAnonimize
        - dc (pydicom)                  : Archivo de la clase pydicom
        - PatientName (String)          : Nombre del paciente
        - PatientID (String)            : ID del paciente
        - PatientBirthDate (String)     : Fecha de Nacimiento del paciente
        - PatientSex (String)           : Sexo del paciente
        - StudyDate (String)            : Fecha en la que se realizó el estudio
        - StudyTime (String)            : Tiempo que tardó el estudio
        - InstitutionName (String)      : Nombre de la institución que realizó el estudio
        - InstitutionAdress (String)    : Dirección de la institución en la que se realizó el estudio.
        
    Valores Defecto:
        - PatientName (String)          : Desconocido
        - PatientID (String)            : Nan
        - PatientBirthDate (String)     : Nan
        - PatientSex (String)           : Nan
        - StudyDate (String)            : Nan
        - StudyTime (String)            : Nan
        - InstitutionName (String)      : Nan
        - InstitutionAdress (String)    : Nan
    """
