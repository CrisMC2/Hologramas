from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QLabel

class AbsTextControl(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_data(self) -> str:
        pass
    
    @abstractmethod
    def change_data(self, new_data: str):
        pass