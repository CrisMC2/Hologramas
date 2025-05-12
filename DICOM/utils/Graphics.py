from typing import Union, overload
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsWidget, QGraphicsLinearLayout, QGraphicsProxyWidget, QWidget, QLayout, QFrame, QSizePolicy, QGraphicsPixmapItem
from PyQt5.QtGui import QBrush, QPainter, QColor
from PyQt5.QtCore import Qt, QRectF

from abstracts.Ui.AbsGraphics import AbsGraphicsView, AbsGraphicsScene, AbsGraphicsWidget, AbsGraphicsProxyWidget


class GraphicsView(AbsGraphicsView):
    def __init__(self):
        super().__init__()
    
    def configure_features(self, scroll_bar_policy: Qt.ScrollBarPolicy,
                           frame_style: QFrame.Shape):
        self.setHorizontalScrollBarPolicy(scroll_bar_policy)
        self.setVerticalScrollBarPolicy(scroll_bar_policy)
        # self.setBackgroundBrush(background)
        self.setFrameStyle(frame_style)
    
    def configure_behaivor(self, size_policy: QSizePolicy, drag, interactive: bool, resize_anchor: QGraphicsView.ViewportAnchor, 
                           portUpdateMode: QGraphicsView.ViewportUpdateMode):
        self.setSizePolicy(size_policy, size_policy)
        self.setDragMode(drag)
        self.setInteractive(interactive)
        self.setResizeAnchor(resize_anchor)
        self.setViewportUpdateMode(portUpdateMode)
    
    """
    El método "configure_behaivor" permite configurar el comportamiento del QGraphicsView.
    
    - Parámetros
        - drag (QGraphicsView.DragMode)  : Permite arrastrar o no una pestaña
        - interactive (bool)             : Permite habilitar la interactividad con la pestaña 
        
    """
    
    def insert_element(self, scene: QGraphicsScene):
        self.setScene(scene)
        
    """
    El método insert_element heredado en la clase GraphicsView
    tiene como función "setear" la escena del GraphicsView.
    
    - Parámetros:
        - self (GraphicsView)       : Instancia de la clase GraphicsView
        - scene (QGraphicsScene)    : Objeto de la clase QGraphicsScene que será usado en el QGraphicsView
    
    """
    
    #Propio de QGraphicsView
    def resizeEvent(self, event):
        super().resizeEvent(event)
        
        self.center_scene_in_view()

        if hasattr(self.scene(), "cover_visible_area"):
            print("Funcion==============")
            self.scene().cover_visible_area(self.mapToScene(self.viewport().rect()).boundingRect())

    """
    El método resizeEvent, propio de la clase QGraphicsView, cumple la función de responsividad.
    
    - Si bien el QGraphicsView se adaptará al tamaño del layout al que esté adjuntado, sus elementos dentro no lo harán.
        Por ello se sobreescribe el método resizeEvent, dejando su naturaleza original (super()), pero agregando acciones
        cada que pase un redimensionado.
        
    """  
    
    def center_scene_in_view(self):
        # center_x, center_y = self.scene().width()/2, self.scene().height()/2
        center = self.scene().sceneRect().center()
        self.centerOn(center)
        print("\n\n\n")
        # print(center_x, center_y)
        
        print("\n\n\n")
        print("Medidas: ",self.scene().width(), self.scene().height())
    
    

    
class GraphicsScene(AbsGraphicsScene):
    def __init__(self):
        super().__init__()
        self.scene_layout = SceneLayoutHelper(self)
    
    def configure_features(self, size: tuple[int, int], scene_rect: tuple[int, int, int, int]):
        # self.q_scene.setSceneRect(0, 0, size[0], size[1])
        # self.q_scene.setSceneRect(scene_rect[0], scene_rect[1], scene_rect[2], scene_rect[3])
        # bounding = self.q_scene.itemsBoundingRect()
        # bounding.setTop(0)
        pass
    """"
    - Parámetros:
        - scene_rect (tuple) => x, y, w, h
        - background (QBrush) => 
    """
    
    def configure_behaivor(self, item_index_method: QGraphicsScene.ItemIndexMethod):
        self.setItemIndexMethod(item_index_method)

    @overload
    def insert_element(self, main_widget: QGraphicsWidget) -> None: ...
        
    @overload
    def insert_element(self, widget: QGraphicsProxyWidget) -> None: ...
    
    @overload
    def insert_element(self, widget: QGraphicsPixmapItem) -> None: ...
    
    def insert_element(self, widget: Union[QGraphicsWidget, QGraphicsProxyWidget, QGraphicsPixmapItem]):
        if isinstance(widget, QGraphicsWidget):
            self.main_widget = widget
            
        self.addItem(widget)
        
        self.scene_layout.center_widget(widget)

    """
    El método "insert_element" heredado en la clase GraphicsScene
    tiene por función añadir a un GraphicsWidget
    
    - Parámetros:
        - self (GraphicsScene)  : Instancia de la clase GraphicsScene
        - element (QWidget)     : Elemento GraphicsWidget (Layout) que será añadido al GraphicsScene
    
    """
    
    def cover_visible_area(self, visible_area: QRectF):
        print("Visible_Area: ", visible_area)
        self.main_widget.setPreferredSize(visible_area.size())
        self.main_widget.resize(visible_area.size())
        
        # self.scene_layout.center_all_widgets()    
    
class SceneLayoutHelper():
    def __init__(self, scene: QGraphicsScene):
        self.scene = scene
        
    def center_widget(self, widget: Union[QGraphicsWidget, QGraphicsProxyWidget, QGraphicsPixmapItem] = None):
        if not widget:
            raise TypeError("El elemento widget que intentas centrar no ha sido especificado, es None.")
        
        scene_rect = self.scene.sceneRect().center()
        bounding = widget.boundingRect().center()
        
        mapScene = widget.mapToScene(bounding)
        
        offset = scene_rect - mapScene
        # bounding_center = bounding.center()

        # center_x = (scene_rect.width() - bounding.width())/2
        # center_y = (scene_rect.height() - bounding.height())/2
                
        widget.setPos(widget.pos()+offset)
    
    def center_all_widgets(self):
        if isinstance(self.scene, QGraphicsScene):
            for item in self.scene.items():
                if isinstance(item, (QGraphicsWidget, QGraphicsProxyWidget, QGraphicsPixmapItem)):
                    self.center_widget(item)

        
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
        self.setLayout(self.q_layout)   #Seteamos el layout al widget

    def configure_features(self, minimum_size_x: int, minimum_size_y: int, size_policy: QSizePolicy):
        self.setMinimumSize(minimum_size_x, minimum_size_y)
        self.setSizePolicy(size_policy, size_policy)
    
    def configure_behaivor(self, size_policy: QSizePolicy):
        self.setSizePolicy(size_policy, size_policy)

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

    # def paint(self, painter, option, widget = None):
    #     rect = self.boundingRect()
    #     painter.setBrush(QBrush(QColor("black")))
    #     painter.setPen(QColor("black"))  # opcional: borde
    #     painter.drawRect(rect)
    
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