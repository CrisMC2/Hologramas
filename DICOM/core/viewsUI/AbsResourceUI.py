from abc import ABC, abstractmethod
import numpy as np
   
class AbsPixmap(ABC):
    @abstractmethod
    def create_pixmap(self, img_array: np.uint8):
        pass
    
    @abstractmethod
    def prepare_array(self, img_array: np.uint8):
        pass    