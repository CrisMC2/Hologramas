from functools import partial
from PyQt5.QtCore import QThread, QObject

from Shared.classes.SignalData import Emit_Data

class WorkerThread(QObject):
    def __init__(self):
        super().__init__()
        self.emit_data = Emit_Data()

    def run(self, func, func_return: bool=False):
        if func_return:
            result = func()
            print(result)
            self.emit_data.emit_signal(result)
        
        else:
            func()
    
class ExtraThread(QObject):
    def __init__(self):
        super().__init__()
        self.worker  = None
        self.thread_ = None
        self._running = True
    
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
            self.worker.emit_data.obj_signal.connect(func)
    
    def finish_(self):
        if self.worker:
            self.worker.canceled = True
        
        if self.thread_ and self.thread_.isRunning():
            self.thread_.quit()
            self.thread_.wait()
            
            self.thread_.finished.connect(self.thread_.deleteLater)
            self.thread_.finished.connect(self.worker.deleteLater)
    
    def stop(self):
        self._running = False
        if not self.thread_.wait(1000):
            # Si no termina a tiempo, lo terminamos de forma forzada
            self.finish_()       