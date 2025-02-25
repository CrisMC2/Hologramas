import os
import sys

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) #Agregamos una carpeta por encima
sys.path.append(_append)

from PyQt5.QtCore import QObject, pyqtSignal

from core.classes.AbsSignal import AbsEmisor, AbsReceptor
class Emisor_text(AbsEmisor):
    señal_str = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        
    def emit_signal(self, signal: str):
        self.señal_str.emit(signal)
    
class Receptor_text(AbsReceptor):
    def __init__(self):
        super().__init__()
        self.receiver_item = ""
    
    def recept_signal(self, signal: str):
        self.receiver_item = signal
    