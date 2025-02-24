from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5 import QtWidgets

class AbsGraphicsView(ABC):
    """
    En este caso directamente generamos al inicio el objeto QGraphicsView
    debido a que sobre este se ejecutarán todos los métodos.
    
    """
    def __init__(self):
        self.graphics_view = QGraphicsView
    
    @abstractmethod
    def configure_features_view(self):
        pass
    
class AbsGraphicsScene(ABC):
    """
    Aquí generamos el objeto QGraphicsScene sobre el cual se ejecutarán 
    todos los métodos
    
    """
    def __init__(self):
        self.graphics_scene = QGraphicsScene
    
    @abstractmethod
    def configure_features_scene(self):
        pass
    
    @abstractmethod
    def configure_behaivor_scene(self):
        pass
    
    @abstractmethod
    def insert_element(self, element: QtWidgets):
        pass