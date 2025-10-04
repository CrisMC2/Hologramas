from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget

from UI_Dicom.core.metaClasses.MetaAbsQt import MetaAbsQt

class AbsUploadData(ABC, QWidget, metaclass= MetaAbsQt):
    """
    No olvidar la inicialización de la clase padre en la clase hija:
        - super().__init__()
    """
    
    @abstractmethod
    def upload(self):
        pass
    
    @abstractmethod
    def get_directory(self):
        pass
    
    @abstractmethod
    def clean_directory(self, *args, **kwargs):
        pass
    
    """
    clean_directory está pensado para que pueda trabajar o con elementos str o 
    list
    """