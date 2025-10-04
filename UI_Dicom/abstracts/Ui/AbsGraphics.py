#Importación de partes de librerías
from abc import abstractmethod
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsWidget, QGraphicsProxyWidget

#Importación de clases del mismo proyecto
from UI_Dicom.core.metaClasses.MetaAbsQt import MetaAbsQt
from UI_Dicom.abstracts.Ui.AbsContainers import AbsContainers
    
class AbsGraphicsView(QGraphicsView, AbsContainers, metaclass=MetaAbsQt):
    def __init__(self):
        super().__init__()
    """
    En este caso directamente generamos al inicio el objeto QGraphicsView
    debido a que sobre este se ejecutarán todos los métodos.
    
    """


class AbsGraphicsScene(QGraphicsScene, AbsContainers, metaclass=MetaAbsQt):
    def __init__(self):
        super().__init__()
    """
    Aquí generamos el objeto QGraphicsScene sobre el cual se ejecutarán 
    todos los métodos
    
    """
        
class AbsGraphicsWidget(QGraphicsWidget, AbsContainers, metaclass=MetaAbsQt):
    def __init__(self):
        # self.q_widget = QGraphicsWidget()
        super().__init__()
    
    """
    En esta parte generamos una instancia del elemento QGraphicsWidget
    """
    
    @abstractmethod
    def convert_correct_type_element(self, element):
        pass
    
class AbsGraphicsProxyWidget(AbsContainers):
    """
    La clase abstracta AbsGraphicsProxyWidget tiene por finalidad
    """
    def __init__(self):
        self.q_proxy_widget = QGraphicsProxyWidget()