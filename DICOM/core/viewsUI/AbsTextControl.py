from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QLabel

class AbsTextControl(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass
    
    @abstractmethod
    def change_info(self, new_data: str):
        pass