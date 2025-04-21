from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal

from core.metaClasses.MetaAbsQt import MetaAbsQt

class AbsEmisor(QWidget, metaclass= MetaAbsQt):
    """

    """

    #Instancia de pyqtSignal usado para la emisión de información
    obj_signal = pyqtSignal(object)
    
    @abstractmethod
    def emit_signal(self, *args, **kwargs):
        pass

class AbsReceptor(QWidget, metaclass= MetaAbsQt):
    
    """
    Asegúrate de que "receiver_item" y "signal" sean del mismo tipo de dato.
    """
    @abstractmethod
    def recept_signal(self, *args, **kwargs):
        pass