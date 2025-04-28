from typing import Union
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLinearLayout, QGraphicsProxyWidget, QWidget, QLayout, QFrame, QSizePolicy
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt, QRectF

from abstracts.Ui.AbsGraphics import AbsGraphicsView, AbsGraphicsScene, AbsGraphicsWidget, AbsGraphicsProxyWidget


class GraphicsView(AbsGraphicsView):
    def __init__(self):
        super().__init__()
    
    def configure_features(self, scroll_bar_policy: Qt.ScrollBarPolicy, background: QBrush, 
                           frame_style: QFrame.Shape):
        self.q_view.setHorizontalScrollBarPolicy(scroll_bar_policy)
        self.q_view.setVerticalScrollBarPolicy(scroll_bar_policy)
        self.q_view.setBackgroundBrush(background)
        self.q_view.setFrameStyle(frame_style)
    
    def configure_features_scene(self, scene: QGraphicsScene, scene_rect: QRectF, center_on: bool, fit_in_view: bool):
        self.q_view.setSceneRect(scene_rect)
        
        if center_on:
            self.q_view.centerOn(scene_rect.center())
        elif fit_in_view:
            self.q_view.fitInView(scene_rect, Qt.KeepAspectRatio)
    
    def configure_behaivor(self, size_policy: QSizePolicy, drag, interactive: bool, resize_anchor: QGraphicsView.ViewportAnchor, 
                           portUpdateMode: QGraphicsView.ViewportUpdateMode):
        # self.q_view.setSizePolicy(size_policy, size_policy)
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
    
    
    def configure_features(self, size: tuple[int, int], scene_rect: tuple[int, int, int, int], background: QBrush):
        # self.q_scene.setSceneRect(0, 0, size[0], size[1])
        # self.q_scene.setSceneRect(scene_rect[0], scene_rect[1], scene_rect[2], scene_rect[3])
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
    def __init__(self, layout: QLayout):
        super().__init__()
        self.q_layout = layout #Establecemos el Layout como parte de la clase
        self.q_widget.setLayout(self.q_layout)   #Seteamos el layout al widget
        
    def configure_features(self, geometry: QGraphicsScene):
        self.q_widget.setGeometry(geometry.sceneRect())
    
    def configure_behaivor(self, size_policy: QSizePolicy):
        self.q_widget.setSizePolicy(size_policy, size_policy)

    def insert_element(self, elements: Union[list[QWidget], list[QGraphicsProxyWidget], list[QLayout]]):            
        for element in elements:
            ele = self.convert_correct_type_element(element)
            self.q_layout.addItem(ele)     
    """
    El método "insert element" permite agregar una serie de elementos al layout que representa el GraphicsWidget
    
    - Parámetros:
        - elements (list[QWidget]) : Lista de elementos derivados de QWidget (QLabel, QTextEdit, QSlider, etc.)
                                        que serán agregados al Layout. 
    
    """  
    
    def convert_correct_type_element(self, element: QWidget):
        if isinstance (element, QWidget) and not isinstance(element, QGraphicsProxyWidget):
            proxy = QGraphicsProxyWidget()
            proxy.setWidget(element)
        
        elif isinstance(element, (QLayout, QGraphicsLinearLayout)):
            proxy = element
        
        else:
            raise ValueError("El tipo de dato del elemento no corresponde a QWidget")
        
        return proxy

    """
    El método convert_correct_type_element, propio de la clase GraphicsWidget
    cumple la función de convertir a los elementos en uno compatible con el contenedor
    QGraphicsWidget.
    
    - Parámetros:
        - self (GraphicsWidget)     : Instancia de la clase GraphicsWidget
        - element (QWidget)         : Elemento que se desea hacer compatible con GraphicsWidget
        
    - Ejemplos:
        - Supongamos que queremos insertar un elemento QLabel en un contenedor
            QGraphicsWidget. Si hacemos la inserción sin cambiar el tipo de elemento QLabel 
            tendríamos un error, debido a que QGraphicsWidget no admite el tipo de elemento QLabel.
            En su lugar, deberíamos utilizar un tipo de elemento QGraphicsProxyWidget, que sí es compatible.
            
            Por ello, si deseamos insertar el elemento QLabel, debemos primero crear un elemento QGraphicsProxyWidget, 
            en este insertaremos el elemento QLabel, y luego añadiremos el elemento QGraphicsProxyWidget en el QGraphicsWidget.

    """
    
class GraphicsProxyWidget(AbsGraphicsProxyWidget):
    def __init__(self):
        super().__init__()
    
    def configure_features(self, position_x: int, position_y: int):
        self.q_proxy_widget.setPos(position_x, position_y)
    
    def configure_behaivor(self, flag: bool):
        self.q_proxy_widget.setFlag(flag)
    
    def insert_element(self, element: QWidget):
        if element:
            self.q_proxy_widget.setWidget(element)
    
    """
    La instancia del método insert_element en la clase GraphicsProxyWidget
    tiene por finalidad setear el widget correspondiente al QGraphicsProxyWidget.
    
    - Ello significa que no se esperan múltiples argumentos, sino que solo uno que sea
        como el layout (único) que posee un widget.
        
    - Parámetros:
        - self (GraphicsProxyWidget):   Instancia de la clase GraphicsProxyWidget    
        - element (QWidget)     :       Elemento de tipo Widget que será insertado en el QGraphicsProxyWidget
        
    """