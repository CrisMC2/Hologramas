import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from typing import Union
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLinearLayout, QGraphicsProxyWidget, QWidget
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt

from core.viewsUI.AbsGraphics import AbsGraphicsView, AbsGraphicsScene, AbsGraphicsWidget


class GraphicsView(AbsGraphicsView):
    def __init__(self):
        super().__init__()
    
    def configure_features(self, background: QBrush, frame_style):
        # self.graphics_view.set
        self.q_view.setBackgroundBrush(background)
        self.q_view.setFrameStyle(frame_style)
        

    def configure_behaivor(self, drag, interactive: bool, resize_anchor: QGraphicsView.ViewportAnchor, portUpdateMode: QGraphicsView.ViewportUpdateMode):
        self.q_view.setDragMode(drag)
        self.q_view.setInteractive(interactive)
        self.q_view.setResizeAnchor(resize_anchor)
        self.q_view.setViewportUpdateMode(portUpdateMode)
    
        """
    El método permite configurar una vista.
    
    - Parámetros
        - drag (QGraphicsView.DragMode)  : Permite arrastrar o no una pestaña
        - interactive (bool)             : Permite habilitar la interactividad con la pestaña 
        
    
    """
    
    def insert_element(self, scene: QGraphicsScene):
        self.q_view.setScene(scene)
        
    """
    El método insert_element heredado en la clase GraphicsView
    tiene como función "setear" la escena del GraphicsView.
    
    - Parámetros:
        - self (GraphicsView)       : Instancia de la clase GraphicsView
        - scene (QGraphicsScene)    : Objeto de la clase QGraphicsScene que será usado en el QGraphicsView
    
    """
    
class GraphicsScene(AbsGraphicsScene):
    def __init__(self):
        super().__init__()
    
    
    def configure_features(self, scene_rect: tuple[int], background: QBrush):
        self.q_scene.setSceneRect(scene_rect[0], scene_rect[1], scene_rect[2], scene_rect[3])
        self.q_scene.setBackgroundBrush(background)
    """"
    - Parámetros:
        - scene_rect (tuple) => x, y, w, h
        - background (QBrush) => 
    """
    
    def configure_behaivor(self, item_index_method: QGraphicsScene.ItemIndexMethod):
        self.q_scene.setItemIndexMethod(item_index_method)

    
    
    def insert_element(self, element: QWidget):
        self.q_scene.addItem(element)

    """
    El método "insert_element" heredado en la clase GraphicsScene
    tiene por función añadir a un GraphicsWidget
    
    - Parámetros:
        - self (GraphicsScene)  : Instancia de la clase GraphicsScene
        - element (QWidget)     : Elemento GraphicsWidget (Layout) que será añadido al GraphicsScene
    
    """

class GraphicsWidget(AbsGraphicsWidget):  
    """
    Constructor de la clase QGraphicsWidget.
    
    - Se instancia al constructor de la clase padre (Para tener disponible al QGraphicsWidget) 
    - Se referencia al método create_layout, pasándole un parámetro.
    
    - Parameters:
        - type_layout (str)     : Define si el método create_layout creará un layout vertical u horizontal.
                                    if   "H" => Horizontal
                                    elif "V" => Vertical
    
    """  
    def __init__(self, type_layout: str):
        super().__init__()
        
        self.create_layout(type_layout)
              
    def create_layout(self, type_layout: str):
        if type_layout == "V":
            self.layout = QGraphicsLinearLayout(Qt.Vertical) #Debido a que estamos usando un QGraphicsWidget, necesitamos del QGraphicsLinearLayout
        
        elif type_layout == "H":
            self.layout = QGraphicsLinearLayout(Qt.Horizontal)
        
        else:
            raise ValueError("El parámetro type_layout debe ser:\n- V if Layout == Vertical\n- H elif Layout == Horizontal")
        
    """
    El método create_layout nos sirve para crear el Layout que cumplirá el labor del 
    GraphicsWidget. 
    
    - La creación del mismo varía de acorde al parámetro type_layout.
    
    - Parámetros:
        - type_layout (str)       : Define si el Layout será vertical u horizontal
    
    """ 
    
    def configure_features(self):
        pass
    
    def configure_behaivor(self):
        pass

    def insert_element(self, elements: Union[list[QWidget], list[QGraphicsProxyWidget]]):
        if self.layout != None:
            
            for element in elements:
                ele = self.convert_correct_type_element(element)
                self.layout.addItem(ele)
            
            self.q_widget.setLayout(self.layout)
        
        else:
            print("Llamar a la función config_layout para generar el layout de los elementos.")
    
    """
    El método "insert element" permite agregar una serie de elementos al layout que representa el GraphicsWidget
    
    - Parámetros:
        - elements (list[QWidget]) : Lista de elementos derivados de QWidget (QLabel, QTextEdit, QSlider, etc.)
                                        que serán agregados al Layout. 
    
    """  
    
    def convert_correct_type_element(self, element: QWidget):
        if isinstance (element, QWidget):
            proxy = QGraphicsProxyWidget()
            proxy.setWidget(element)
        
        else:
            raise ValueError("El tipo de dato del elemento no corresponde a QWidget")
        
        return proxy