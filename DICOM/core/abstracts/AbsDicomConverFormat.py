from abc import ABC, abstractmethod

class AbsDicomConvert(ABC):
    @abstractmethod
    def convert_dicom(self):
        pass    
    
    @abstractmethod
    def save_convert(self):
        pass
    
    @abstractmethod
    def extract_features(self):
        pass
 
class AbsFeaturesVideo(ABC):
    @abstractmethod
    def define_shape(self):
        pass
    
    @abstractmethod
    def define_mode(self, format: str):
        pass
    
    @abstractmethod
    def define_codec(self):
        pass
    