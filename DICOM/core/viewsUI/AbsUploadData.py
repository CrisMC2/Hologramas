from abc import ABC, abstractmethod

class AbsUploadData(ABC):
    @abstractmethod
    def upload(self):
        pass
    
    @abstractmethod
    def get_directory(self):
        pass
    
    @abstractmethod
    def clean_directory(self, directory: str):
        pass

    @abstractmethod
    def clean_directory(self, directory: list):
        pass