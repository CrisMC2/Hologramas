import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from abstracts.Ui.AbsContainers import AbsContainers

from PyQt5.QtWidgets import QWidget, QLayout, QGraphicsProxyWidget

class Widget(AbsContainers):
    def __init__(self):
        self.q_widget = QGraphicsProxyWidget()
        # self.q_widget = QWidget()
    
    def configure_features(self, margin_left: int = 0, margin_top: int = 0, 
                           margin_right: int = 0, margin_bottom: int = 0):
        self.q_widget.setContentsMargins(margin_left, margin_top,
                                         margin_right, margin_bottom)
    
    def configure_behaivor(self, *args, **kwargs):
        pass
    
    def insert_element(self, widget: QWidget):
        if isinstance(widget, (QLayout, QWidget)):
            self.q_widget.setWidget(widget)
            
    """
    La instancia del método "insert_element" en la clase Widget
    permite insertar un layout en el elemento Widget.
    
    El método no cambia de nombre ni de instancia debido a que en un elemento QWidget solo 
    se puede insertar un layout.
    """