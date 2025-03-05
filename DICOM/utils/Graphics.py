import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QBrush

from core.viewsUI.AbsGraphics import AbsGraphicsView, AbsGraphicsScene, AbsGraphicsWidget


class GraphicsView(AbsGraphicsView):
    def __init__(self):
        super().__init__()
    
    def configure_features(self, background: QBrush, frame_style):
        self.graphics_view.set
        self.graphics_view.setBackgroundBrush(background)
        self.graphics_view.setFrameStyle(frame_style)
        
    """
    El método permite configurar una vista.
    
    - Parámetros
        - drag (QGraphicsView.DragMode)  : Permite arrastrar o no una pestaña
        - interactive (bool)             : Permite habilitar la interactividad con la pestaña 
        
    
    """
    def configure_behaivor(self, drag, interactive: bool, resize_anchor: QGraphicsView.ViewportAnchor, portUpdateMode: QGraphicsView.ViewportUpdateMode):
        self.graphics_view.setDragMode(drag)
        self.graphics_view.setInteractive(interactive)
        self.graphics_view.setResizeAnchor(resize_anchor)
        self.graphics_view.setViewportUpdateMode(portUpdateMode)
    
class GraphicsScene(AbsGraphicsScene):
    def __init__(self):
        super().__init__()
    
    """"
    - Parámetros:
        - scene_rect (tuple) => x, y, w, h
    """
    def configure_features(self, scene_rect: tuple[int], background: QBrush):
        self.graphics_scene.setSceneRect(scene_rect[0], scene_rect[1], scene_rect[2], scene_rect[3])
        self.graphics_scene.setBackgroundBrush(background)
    
    def configure_behaivor(self, item_index_method: QGraphicsScene.ItemIndexMethod):
        self.graphics_scene.setItemIndexMethod(item_index_method)

    
    """
    En este caso los elementos son una lista, la cual no especificamos los tipos.
    
    La lista de elementos puede ser de distintos.
    
    """
    def insert_element(self, element: QWidget):
        self.graphics_scene.addItem(element)


class GraphicsWidget(AbsGraphicsWidget):
    def configure_features(self):
        pass
    
    def configure_behaivor(self):
        pass
    
    """
    El parámetro type_layout nos sirve para determinar qué tipo de layout 
    usaremos con el GraphicsWidget.
    
    - Parámetros:
        - type_layout       : Define si el Layout será vertical u horizontal
    
    """
    def config_layout(self, type_layout):
        if type_layout == "V":
            self.layout = QVBoxLayout()
        
        elif type_layout == "H":
            self.layout = QHBoxLayout()
        
    def insert_element(self, elements: list):
        if self.layout != None:
            
            for element in elements:
                self.layout.addWidget(element)
            
            self.graphics_widget.setLayout(self.layout)
        
        else:
            print("Llamar a la función config_layout para generar el layout de los elementos.")