import os
import sys

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(_append)

from abc import ABC, abstractmethod
from PyQt5.QtCore import QObject, pyqtSignal

from core.metaClasses.MetaAbsQt import MetaAbsQt

class AbsEmisor(ABC, QObject, metaclass= MetaAbsQt):
    @abstractmethod
    def emit_signal(self, signal):
        pass

class AbsReceptor(ABC, QObject, metaclass= MetaAbsQt):
    
    """
    Asegúrate de que "receiver_item" y "signal" sean del mismo tipo de dato.
    """
    @abstractmethod
    def recept_signal(self, receiver_item, signal):
        pass