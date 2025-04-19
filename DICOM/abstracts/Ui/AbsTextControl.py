import sys
import os

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