#Importación de Librerías
import numpy as np

#Importación de partes de librerías
from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget

#Importación de clases del mismo proyecto
from abstracts.Ui.AbsContainers import AbsContainers   

class AbsUi_Pixmap(AbsContainers):
    """
    La clase AbsUi_Pixmap tiene como función permitirnos trabajar de manera gráfica
    con los elementos QPixmap.
    
    - Siendo sus funciones poder mostrar un elemento Pixmap para su utilización 
        en la interfaz gráfica después de previamente haberlo creado y procesado.
    
    - Herencia:
        - AbsContainers     : Clase abstracta especializada para la configuración de contenedores.
    
    - Métodos:
        - define_container (abstractmethod)                 : Método enfocado al contenedor que acogerá 
                                                                el elemento Pixmap
        - configure_features (abstractmethod) (Heredado)    : Método enfocado a las características del contenedor
        - configure_behaivor (abstractmethod) (Heredado)    : Método enfocado al comportamiento del contenedor
        - insert_element (abstractmethod) (Heredado)        : Método enfocado a la inserción de elementos 
                                                                en los contenedores
    
    """
    
    @abstractmethod
    def define_container(self, container: QWidget):
        pass
    """
    El método define_container tiene como objetivo
    definir cuál será el contenedor sobre el cual se trabajará con
    el elemento Pixmap en la interfaz visual.
    
    - Parámetros:
        - container (QWidget)     : Este elemento acogerá al elemento Pixmap.
        
    """
    
class AbsProccessPixmap(ABC):
    @abstractmethod
    def create_pixmap(self, img_array: np.uint8):
        pass
    
    @abstractmethod
    def prepare_array(self, img_array: np.uint8):
        pass    
