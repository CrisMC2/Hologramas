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
    def __init__(self):
        self.q_view = QGraphicsView()

    """
    En este caso directamente generamos al inicio el objeto QGraphicsView
    debido a que sobre este se ejecutarán todos los métodos.
    
    """

class AbsGraphicsScene(AbsGraphics):
    def __init__(self):
        self.q_scene = QGraphicsScene()
    """
    Aquí generamos el objeto QGraphicsScene sobre el cual se ejecutarán 
    todos los métodos
    
    """
    
class AbsGraphicsWidget(AbsGraphics):
    def __init__(self):
        self.q_widget = QGraphicsWidget()
    
    """
    En esta parte generamos una instancia del elemento QGraphicsWidget
    """
    
    @abstractmethod
    def create_layout(self):
        pass
    
    @abstractmethod
    def convert_correct_type_element(self, element):
        pass