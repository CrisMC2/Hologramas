from functools import partial
from PyQt5.QtCore import QThread, QObject

from Gestures.controller.CreateModel import create_model
from Shared.classes.SignalData import Emit_Data

class WorkerThread(QObject):
    def __init__(self):
        super().__init__()
        self.emit_data = Emit_Data()

    def run(self, func, func_return: bool):
        if func_return:
            result = func()
            self.emit_data.emit_signal(result)
        
        else:
            func()
    
class ExtraThread():
    def __init__(self):
        self.worker  = None
        self.thread_ = None
    
    def start_(self, func, func_return: bool=False):
        if not self.worker and not self.thread_:
            self.worker = WorkerThread()
            self.thread_ = QThread()
        
        self.worker.moveToThread(self.thread_)
     
        function_ = partial(self.worker.run, func=func, func_return=func_return)
        self.thread_.started.connect(function_)
        self.finish_()
        self.thread_.start()
        
    def finish_(self):
        self.thread_.quit()
        self.thread_.finished.connect(self.worker.deleteLater)
        self.thread_.finished.connect(self.thread_.deleteLater)
    
    def connect_signal(self, func):
        if self.worker:
            self.worker.emit_data.obj_signal.connect(func)