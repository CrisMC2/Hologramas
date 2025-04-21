from PyQt5.QtCore import pyqtSignal

from abstracts.classes.AbsSignal import AbsEmisor, AbsReceptor

class Emit_Data(AbsEmisor):
    """"
    El método permite emitir una señal de tipo de dato string.
    
    - Parámetros: 
        - Signal (str)  : Tipo de dato String que se emitirá.
    
    - Retorno:
        - pyqtSignal.emit() : La señal se emite.
        
    """    
    def __init__(self):
        super().__init__() #Aquí también se define el elemento self.obj_signal

    def emit_signal(self, signal: object):
        self.signal_str.emit(signal)

class Recept_Data(AbsReceptor):
    """
    El método permite recibir una señal, la cual está pensada para que sea un dato de
    tipo string
    
    - Parámetros:
        - signal (str) : Variable de tipo String que representa la señal
    
    """
    def __init__(self):
        super().__init__()
    
    def recept_signal(self, signal: object):
        self.receiver_item = signal

    