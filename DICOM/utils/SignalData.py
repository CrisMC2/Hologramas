from PyQt5.QtCore import pyqtSignal

from abstracts.classes.AbsSignal import AbsEmisor, AbsReceptor

class Emisor_text(AbsEmisor):
    """"
    El método permite emitir una señal de tipo de dato string.
    
    - Parámetros: 
        - Signal (str)  : Tipo de dato String que se emitirá.
    
    - Retorno:
        - pyqtSignal.emit() : La señal se emite.
        
    """
    signal_str = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
    
    
    def emit_signal(self, signal: str):
        self.signal_str.emit(signal)

class Emisor_list(AbsEmisor):
    """
    El método permite emitir una señal con un dato de tipo lista.
    
    - Parámetros:
        - signal (list)  : Elemento de tipo list que será emitido.
    
    - Retorno:
        - pyqtSignal.emit() : La señal se emite.
    
    """
    signal_list = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
    

    def emit_signal(self, signal: list):
        self.signal_list.emit(signal)
    
class Receptor_text(AbsReceptor):
    """
    El método permite recibir una señal, la cual está pensada para que sea un dato de
    tipo string
    
    - Parámetros:
        - signal (str) : Variable de tipo String que representa la señal
    
    """
    def __init__(self):
        super().__init__()
        self.receiver_item = ""
    
    def recept_signal(self, signal: str):
        self.receiver_item = signal

    