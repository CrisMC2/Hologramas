import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from PyQt5.QtWidgets import QApplication, QMainWindow #No eliminar el QApplication, es necesario para el test desde tests.test_subViewDICOM
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

from utils.Graphics import GraphicsView, GraphicsScene, GraphicsWidget
from utils.ElementsWidgets import TextWidget, SliderWidget
from utils.PixmapUi import PixmapUi
from config import constantSubViewDICOM as consVDcm

class Ui_subViewDicom(QMainWindow):
    def __init__(self):
        super().__init__()

        self.generate_containers()
        self.generate_widget()
        self.generate_items()
        
        self.configure_containers()
        self.insert_elements()
    
    def generate_containers(self):
        self.ui_graphics_view   = GraphicsView()
        self.ui_graphics_scene  = GraphicsScene()
        self.ui_graphics_widget = GraphicsWidget(consVDcm.DEFAULT_TYPE_LAYOUT) #Utilizamos la constante del tipo de Layout que tendrá el Widget
        
    def generate_widget(self):
        widget_main = QWidget(self)
        layout = QHBoxLayout(widget_main)
        layout.addWidget(self.ui_graphics_view.q_view)
        
        self.setCentralWidget(widget_main)
        self.setWindowTitle("SubView DICOM")
    """
    COMENTARIO
    - Parámetros:
        mdsmldmaskldmlka
    """ 
    
    def generate_items(self):
        self.ui_text_img = TextWidget(QLabel()) #Generamos un elemento QWidget
        self.ui_text_img_now = TextWidget(QLabel())
        self.ui_text_img_end = TextWidget(QLabel())       
        self.ui_text_name = TextWidget(QLabel())
        self.ui_text_date_born = TextWidget(QLabel())
        self.ui_text_date_test = TextWidget(QLabel())
        self.ui_text_part_body = TextWidget(QLabel())
        
        self.ui_slider = SliderWidget(consVDcm.DEFAULT_TYPE_SLIDER) #Utilizamos la constante del tipo de Slider
        
        self.ui_img_dicom = PixmapUi(QLabel()) #Generamos un contenedor que mostrará al elemento "Pixmap"
    
    """
    El método generate_items está diseñado para generar todos los elementos que 
    la vista de visualización de los DICOM necesita.
    
    - Elementos:
        - ui_text_img (QLabel)          : Instancia de la clase TextWidget encargada de mostrar en forma de texto: Img 
        
        - ui_text_img_now (QLabel)      : Instancia de la clase TextWidget encargada de mostrar en forma de texto
                                            la imagen actual del folder DICOM en la que se encuentra el usuario.
        
        - ui_text_img_end (QLabel)      : Instancia de la clase TextWidget encargada de mostrar en forma de texto
                                            la cantidad de imágenes que hay en el folder DICOM.
        
        - ui_text_name (QLabel)         : Instancia de la clase TextWidget encargada de mostrar en forma de texto
                                            el nombre del paciente al cual pertenece el folder DICOM
        
        - ui_text_date_born (QLabel)    : Instancia de la clase TextWidget encargada de mostrar en forma de texto
                                            la fecha de nacimiento del paciente.
        
        - ui_text_date_test (QLabel)    : Instancia de la clase TextWidget encargada de mostrar en forma de texto
                                            la fecha en la cuál se realizó la prueba (tomografía, etc.) del paciente.
        
        - ui_text_part_body (QLabel)    : Instancia de la clase TextWidget encargada de mostrar en forma de texto
                                            la parte del cuerpo utilizada para el folder DICOM.

        - ui_slider (QSlider)           : Instancia de la clase SliderWidget, definido de forma Vertical y encargado 
                                            del cambio de las imágenes (archivos DICOM) en el folder DICOM.
    """
    
    def configure_containers(self):
        #Configuramos las características del View
        self.ui_graphics_view.configure_features(consVDcm.BACKGROUND_COLOR_DEFAULT, consVDcm.FRAME_STYLE_DEFAULT)
        
        #Configuramos el comportamiento del View
        self.ui_graphics_view.configure_behaivor(consVDcm.DRAG_MODE_DEFAULT, consVDcm.INTERACTIVE_DEFAULT,
                                              consVDcm.RESIZE_ANCHOR_DEFAULT,consVDcm.VIEW_PORT_UPDATE_MODE_DEFAULT)
        
        #Configuramos las características de la Scene
        self.ui_graphics_scene.configure_features(consVDcm.SCENE_RECT_DEFAULT, consVDcm.BACKGROUND_COLOR_DEFAULT_2)
        
        #Configuramos el comportamiento de la Scene
        self.ui_graphics_scene.configure_behaivor(consVDcm.ITEM_INDEX_METHOD_DEFAULT)
        
        #Configuramos las características del GraphicsWidget
        self.ui_graphics_widget.configure_features()
        
        #Configuramos el comportamiento del GraphicsWidget
        self.ui_graphics_widget.configure_behaivor()  
        
    """
    El método permite configurar los containers que tendrá la subInterfaz.
    
    - NOTA:
        - La mayoría de configuraciones provienen del archivo de constantes: config.constantSubViewDICOM, 
            si necesitas entender qué hace cada carecterística revisa el archivo de constantes.
    
    """
    
    def configure_items(self):
        pass
    
    """
    El método configure_items permite configurar los elementos (items) que conforman a la subinterfaz
    
    """

    
    def insert_elements(self):
        #Insertamos la escena en el GraphicsView
        self.ui_graphics_view.insert_element(self.ui_graphics_scene.q_scene)
        
        #Insertamos el GraphicsWidget en el GraphicsScene
        self.ui_graphics_scene.insert_element(self.ui_graphics_widget.q_widget)
        
        #Insertamos todos los elementos necesarios en el GraphicsWidget
        self.ui_graphics_widget.insert_element([self.ui_text_img.q_text, self.ui_text_img_now.q_text, self.ui_text_img_end.q_text,
                                                self.ui_img_dicom.q_pixmap, self.ui_text_name.q_text, self.ui_text_date_born.q_text, 
                                                self.ui_text_date_test.q_text, self.ui_slider.q_slider])
    
    """
    El método insert_elements nos permite poder insertar los elementos necesarios
    en sus respectivos contenedores.
    
    - Inserciones:
        - Graphics_View : En este contenedor insertamos la escena por medio del QGraphicsScene
        - Graphics_Scene: En este contenedor insertamos el Widget por medio del QGraphicsWidget
        - Graphics_Widget: En este contenedor insertamos todos los elementos que conformarán la interfaz.
    
    """