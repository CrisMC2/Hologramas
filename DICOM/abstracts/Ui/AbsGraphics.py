import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(_append)

#Importación de partes de librerías
from abc import abstractmethod
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsWidget

#Importación de clases del mismo proyecto
from abstracts.Ui.AbsContainers import AbsContainers
    
class AbsGraphicsView(AbsContainers):
    def __init__(self):
        self.q_view = QGraphicsView()

    """
    En este caso directamente generamos al inicio el objeto QGraphicsView
    debido a que sobre este se ejecutarán todos los métodos.
    
    """

class AbsGraphicsScene(AbsContainers):
    def __init__(self):
        self.q_scene = QGraphicsScene()
    """
    Aquí generamos el objeto QGraphicsScene sobre el cual se ejecutarán 
    todos los métodos
    
    """
    
class AbsGraphicsWidget(AbsContainers):
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