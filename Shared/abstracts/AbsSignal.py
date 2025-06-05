from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

class AbsEmisor(QWidget): #Es necesario que herede de QWidget
    """

    """
    #Instancia de pyqtSignal usado para la emisión de información
    obj_signal = pyqtSignal(object)
    obj_signal_2 = pyqtSignal(object, object)
    
    @abstractmethod
    def emit_signal(self, *args, **kwargs):
        pass

class AbsReceptor():
    
    """
    Asegúrate de que "receiver_item" y "signal" sean del mismo tipo de dato.
    """
    @abstractmethod
    def recept_signal(self, *args, **kwargs):
        pass