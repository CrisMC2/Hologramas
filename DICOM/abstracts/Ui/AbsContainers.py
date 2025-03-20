from abc import ABC, abstractmethod

class AbsContainers(ABC):
    @abstractmethod
    def configure_features(self):
        pass
    
    @abstractmethod
    def configure_behaivor(self):
        pass
    
    @abstractmethod
    def insert_element(self):
        pass