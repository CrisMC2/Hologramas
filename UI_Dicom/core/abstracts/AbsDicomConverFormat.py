from abc import ABC, abstractmethod

class AbsDicomConvert(ABC):
    @abstractmethod
    def convert_dicom(self, *args, **kwargs):
        pass    
    
    @abstractmethod
    def save_convert(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def extract_features(self, *args, **kwargs):
        pass
 
class AbsFeaturesVideo(ABC):
    @abstractmethod
    def define_shape(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def define_mode(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def define_codec(self, *args, **kwargs):
        pass
    