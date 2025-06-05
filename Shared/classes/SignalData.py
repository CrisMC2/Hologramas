import numpy as np
from typing import overload

from Shared.abstracts.AbsSignal import AbsEmisor, AbsReceptor

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

    @overload
    def emit_signal(self, signal_1: object) -> None : ...
    @overload
    def emit_signal(self, signal_1: object, signal_2: object) -> None : ...
    
    def emit_signal(self, signal_1: object, signal_2:object=None):
        if isinstance(signal_2, np.ndarray):
                if signal_2.any():
                    self.obj_signal_2.emit(signal_1, signal_2)
        else:
            self.obj_signal.emit(signal_1)
        
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

    