from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene


class AbsGraphicsView(ABC):
    @abstractmethod
    def create_graphics_view(self) ->QGraphicsView:
        pass
    
    @abstractmethod
    def configure_features_view(self):
        pass
    
class AbsGraphicsScene(ABC):
    def __init__(self):
        self.graphics_view = QGraphicsView()
    
    @abstractmethod
    def create_graphics_scene(self) -> QGraphicsScene:
        pass
    
    @abstractmethod
    def configure_features_scene(self):
        pass
    
    @abstractmethod
    def configure_behaivor_scene(self):
        pass