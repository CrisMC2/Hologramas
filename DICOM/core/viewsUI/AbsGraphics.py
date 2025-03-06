from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsWidget
from PyQt5 import QtWidgets

class AbsGraphics(ABC):
    @abstractmethod
    def configure_features(self):
        pass
    
    @abstractmethod
    def configure_behaivor(self):
        pass
    
    @abstractmethod
    def insert_element(self):
        pass
    
class AbsGraphicsView(AbsGraphics):
    """
    En este caso directamente generamos al inicio el objeto QGraphicsView
    debido a que sobre este se ejecutarán todos los métodos.
    
    """
    def __init__(self):
        self.graphics_view = QGraphicsView()


class AbsGraphicsScene(AbsGraphics):
    """
    Aquí generamos el objeto QGraphicsScene sobre el cual se ejecutarán 
    todos los métodos
    
    """
    def __init__(self):
        self.graphics_scene = QGraphicsScene()

class AbsGraphicsWidget(AbsGraphics):
    """
    En esta parte generamos una instancia del elemento QGraphicsWidget
    """
    def __init__(self):
        self.graphics_widget = QGraphicsWidget()
        
    @abstractmethod
    def config_layout(self):
        pass