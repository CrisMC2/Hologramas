from abc import ABC, abstractmethod

#Toda la información de DICOM
class AbsDicomInformation (ABC):
    """
    Constructor de la clase AbsDicomInformation
    
    - Genera una instancia de la clase AbsDicomRead()
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
    def anonymize_dicom(self, *args, **kwargs):
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
