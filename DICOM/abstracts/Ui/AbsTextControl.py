import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(_append)

from abc import abstractmethod

from PyQt5.QtWidgets import QLabel

#Importancias de clases del proyecto
from abstracts.Ui.AbsWidget import AbsWidget

class AbsTextControl(AbsWidget):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_data(self) -> str:
        pass
    
    @abstractmethod
    def change_data(self, new_data: str):
        pass