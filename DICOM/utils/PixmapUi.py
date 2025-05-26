from typing import Union
from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsPixmapItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from abstracts.Ui.AbsPixmap import AbsUi_Pixmap

class PixmapUi(AbsUi_Pixmap):
    """
    La clase PixmapUi está especializada para la visualización de elemento QPixmap en una interfaz visual
    basada en Qt.
    
    Esta clase permite determinar el tipo de contenedor que se usará para la visualización del QPixmap.
    
    - Métodos:
        - __init__ (constructor)    : Inicializa la clase.
        - define_container (void)   : Encargado de definir el tipo de contenedor que se usará.
        - configure_features (void) : Encargado de configurar las características que tendrá el contenedor.
        - configure_behaivor (void) : Encargado de configurar el comportamiento que tendrá el contenedor.
        - insert_element (void)     : Encargado de insertar el elemento Pixmap en el contenedor correspondiente.
    
    """
    
    def __init__(self, type_container: QWidget):
        self.define_container(type_container)
    """
    El constructor de la clase PixmapUi define el contenedor que usará la clase.
    
    - Parámetros:
        - type_container (QWidget)  : Este elemento será usado luego para definir el tipo de elemento
                                        que será el container (contenedor).
    
    """
    
    def define_container(self, container: Union[QLabel, QGraphicsPixmapItem]):
        if isinstance(container, (QLabel, QGraphicsPixmapItem)):
            self.q_pixmap = container
        else:
            raise TypeError("El tipo de objeto brindado no es compatible con el elemento Pixmap: Intente con elementos de tipo: QLabel, QGraphicsPixmapItem")
    
    """
    El método define_container nos permite establecer una variable de clase a partir
    de un parámetro que defina que tipo de contenedor usaremos.
    
    - Parámetros:
        - self (PixmapUi)       : Instancia de la clase PixmapUi
        - container (Union[QLabel, QGraphicsPixmapItem])    : Define el contenedor sobre el cual se visualizará el Pixmap
    
    - Ejemplo:
        - container == QLabel   : El QLabel es ideal si queremos una visualización del Pixmap estática.
        - container == QGraphicsPixmapItem  : El elemento QGraphicsPixmapItem es ideal si queremos una visualización
                                                   interactiva del Pixmap (rotar, mover, escalar).
    
    """
    
    def configure_features(self) -> None:
        
        # self.q_pixmap.setFixedSize(size_x, size_y)
        # self.q_pixmap.setMinimumSize(minimum_size_x, minimum_size_y)
        # self.q_pixmap.setSizePolicy(size_policy_x, size_policy_y)     
        pass
    def configure_behavior(self):
        pass
    
    def insert_element(self, pixmap: QPixmap):
        self.q_pixmap.setPixmap(pixmap)
        # self.q_pixmap.setPixmap(pixmap.scaled(self.q_pixmap.width(), self.q_pixmap.height(), Qt.KeepAspectRatio))
        
    """
    El método insert_element permite cargar el elemento Pixmap 
    dentro del contenedor previamente creado.
    
    - Parámetros:
        - self (PixmapUi)   : Instancia de la clase PixmapUi.
        - pixmap (QPixmap)  : Elemento Pixmap que será mostrado. 
    """