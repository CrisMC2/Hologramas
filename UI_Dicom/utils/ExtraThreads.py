from functools import partial
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject, QThread 

from Shared.classes.SignalData import Emit_Data

class WorkerThread(QObject):
    def __init__(self):
        super().__init__()
        self.emit_data = Emit_Data()
        
    def run (self, func, func_return: bool=False):
        if func_return:
            result, result_ = func()
            self.emit_data.emit_signal(result, result_)
    
        else:
            func()
            self.emit_data.emit_signal(func_return)
    """
    El método "run" de la clase MakeThread nos permite realizar el trabajo de una función y
    luego emitir los datos que está función generará o emitir un valor booleano.
    
    - Si func_return == True => Se retorna la función ejecutada (Se supone que está a su vez está 
            hecha para retornar valores)
    - Si func_return == False => Se retorna un valor booleano (True) cuando la función ya se haya ejecutado
    
    - Al utilizar una función como argumento, de cierta manera es tener un decorador.
    
    - Parámetros:
        - self (MakeThread)     => Instancia de la clase MakeThread
        - func (function)       => Función que será ejecutada por el método "run"
        - func_return (bool)    => Argumento necesario para definir si se retornarán los valores de la función dada como argumento
                                    o un valor booleano (True)
    
    Nota => El método solo permite emitir un máximo de 2 elementos.
    """
class MakeThread(QObject):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.thread_ = None

    def start_(self, func, func_return: bool=False):
        self.worker = WorkerThread()
        self.thread_ = QThread()
        self.worker.moveToThread(self.thread_)
        
        function_ = partial(self.worker.run, func=func, func_return=func_return)
        self.thread_.started.connect(function_)
        self.finish_()
        self.thread_.start()
    
    def connect_signal(self, func):
        if self.worker:
            self.worker.emit_data.obj_signal_2.connect(func)
                    
    def finish_(self):
        if self.worker:
            self.worker.canceled = True
        
        if self.thread_ and self.thread_.isRunning():
            self.thread_.quit()
            self.thread_.wait()
            self.thread_.finished.connect(self.thread_.deleteLater)
            self.thread_.finished.connect(self.worker.deleteLater)