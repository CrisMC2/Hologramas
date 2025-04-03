import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

#Importamos partes de librerías
from PyQt5.QtWidgets import QApplication, QMainWindow #No eliminar el QApplication, es necesario para el test desde tests.test_subViewDICOM
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QGraphicsProxyWidget, QGraphicsPixmapItem, QGraphicsLinearLayout, QLayout


#Importamos clases del mismo proyecto (Programa nuestro)
from utils.Graphics import GraphicsView, GraphicsScene, GraphicsWidget
from utils.Layout import LinearLayout, GridLayout
from utils.Widgets import Widget
from utils.ElementsWidgets import TextWidget, SliderWidget
from utils.PixmapUi import PixmapUi
from config import constantSubViewDICOM as consVDcm

class Ui_subViewDicom(QMainWindow):
    def __init__(self, main_container: tuple[QWidget, QLayout]):
        super().__init__()

        self.generate_containers()
        self.generate_items()
        
        self.configure_containers()
        self.insert_elements()
        
        self.setup_sub_view_dicom(main_container[0], main_container[1])
    
    def generate_containers(self):
        self.ui_graphics_view   = GraphicsView()
        self.ui_graphics_scene  = GraphicsScene()
        self.ui_layout_left = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_1) #Utilizamos la constante del tipo de Layout que tendrá el Widget
        self.ui_layout_right_1 = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_1) #Utilizamos la constante del tipo de Layout
        self.ui_layout_right_2 = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_1)
        self.ui_layout_center = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_2)
        
        self.ui_layout_main = GridLayout(consVDcm.DEFAULT_ROWS_LAYOUT, consVDcm.DEFAULT_COLS_LAYOUT)
        
        self.ui_graphics_widget = GraphicsWidget(self.ui_layout_main.q_grid_layout)  #Como layout principal configuramos al GridLayout creado anteriormente
        
        self.ui_widget_left_1 = Widget()
        self.ui_widget_center = Widget()
        self.ui_widget_right_1 = Widget()
        self.ui_widget_right_2 = Widget() #Widgets necesarios para la inserción de los layout y pixmap
        
    
    """
    El método generate_constainers, propio de la clase Ui_subViewDicom,
    está diseñado para generar todos los contenedores que almacenarán a los
    elementos necesarios para la visualización idónea de archivos DICOM.
    
    - Elementos:
        - self.ui_graphics_view (QGraphicsView)     : Contenedor principal, encargado de establecer la base para todos los demás elementos y contenedores.
        - self.ui_graphics_scene (GraphicsScene)    : Contenedor a insertar en el QGraphicsView, encargado de la interacción con cualquier elemento que se agregue.
        - self.ui_layout_left (LinearLayout)        : Contenedor encargado de la ubicación de los elementos (num_image, num_image_now, num_image_end) en el layout principal de la escena.
        - self.ui_layout_right_1 (LinearLayout)     : Contenedor encargado de la ubicación de los elementos (birthday, sex_patient) en el layout principal de la escena.
        - self.ui_layout_right_2 (LinearLayout)     : Contenedor encargado de la ubicación de los elementos (date_test, time_test) en el layout principal de la escena.
        - self.ui_layout_main (GridLayout)          : Contenedor principal del QGraphicsWidget encargado de la ubicación de todos los elementos.
        - self.ui_graphics_widget (GraphicsWidget)  : Contenedor principal del QGraphicsScene, encargado de la distribución de todos los elementos por medio del 
                                                        GridLayout self.ui_layout_main
    
    """   
    def setup_sub_view_dicom(self, MainWidget: QWidget, MainLayout: QLayout):
        MainLayout.addWidget(self.ui_graphics_view.q_view)
        
        self.setCentralWidget(MainWidget)
        self.setWindowTitle("SubView DICOM")
    """
    COMENTARIO
    - Parámetros:
        mdsmldmaskldmlka
    """ 
    
    def generate_items(self):
        self.ui_text_img = TextWidget(QLabel(), QGraphicsProxyWidget()) #Generamos un elemento QWidget
        self.ui_text_img_now = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_img_end = TextWidget(QLabel(), QGraphicsProxyWidget())       
        self.ui_text_name = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_ID_Patient = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_date_born = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_sex = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_institution_name = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_study_ID = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_body_part = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_acquisition_test = TextWidget(QLabel(), QGraphicsProxyWidget())
        self.ui_text_acquisition_time = TextWidget(QLabel(), QGraphicsProxyWidget())
        
        self.ui_slider = SliderWidget(consVDcm.DEFAULT_TYPE_SLIDER) #Utilizamos la constante del tipo de Slider
        
        self.ui_img_dicom = PixmapUi(QGraphicsPixmapItem()) #Generamos un contenedor que mostrará al elemento "Pixmap"
    
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
        self.ui_graphics_view.configure_features(consVDcm.SCROLL_BAR_POLICY_DEFAULT, consVDcm.BACKGROUND_COLOR_DEFAULT, consVDcm.FRAME_STYLE_DEFAULT)
        
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
        
        #Configuramos las características del Layout Izquierdo
        self.ui_layout_left.configure_features(consVDcm.DEFAULT_LEFT_MARGIN, consVDcm.DEFAULT_RIGHT_MARGIN,
                                               consVDcm.DEFAULT_TOP_MARGIN, consVDcm.DEFAULT_BOTTOM_MARGIN,
                                               consVDcm.DEFAULT_SPACING)
        
        #Configuramoas las características del primer Layout Derecho
        self.ui_layout_right_1.configure_features(consVDcm.DEFAULT_LEFT_MARGIN, consVDcm.DEFAULT_RIGHT_MARGIN,
                                                  consVDcm.DEFAULT_TOP_MARGIN, consVDcm.DEFAULT_BOTTOM_MARGIN,
                                                  consVDcm.DEFAULT_SPACING)
        
        
        #Configuramoas las características del segundo Layout Derecho
        self.ui_layout_right_2.configure_features(consVDcm.DEFAULT_LEFT_MARGIN, consVDcm.DEFAULT_RIGHT_MARGIN,
                                                  consVDcm.DEFAULT_TOP_MARGIN, consVDcm.DEFAULT_BOTTOM_MARGIN,
                                                  consVDcm.DEFAULT_SPACING)
        
        #Configuramos las características del Layout Central
        self.ui_layout_center.configure_features(consVDcm.DEFAULT_LEFT_MARGIN, consVDcm.DEFAULT_RIGHT_MARGIN,
                                                 consVDcm.DEFAULT_TOP_MARGIN, consVDcm.DEFAULT_BOTTOM_MARGIN,
                                                 consVDcm.DEFAULT_SPACING)
        
        #Configuramos las características del Layout Principal
        self.ui_layout_main.configure_features(consVDcm.LIST_DICT_ROWS_STRETCH, consVDcm.LIST_DICT_COLS_STRETCH, 
                                               consVDcm.DEFAULT_SPACING_MAIN)
        
        #Configuramos los widget
        self.ui_widget_left_1.configure_features()
        self.ui_widget_right_1.configure_features()
        self.ui_widget_right_2.configure_features()
        self.ui_widget_center.configure_features() #No definimos el tamaño de los márgenes debido a que están establecidos por defecto

        
    """
    El método permite configurar los containers que tendrá la subInterfaz.
    
    - NOTA:
        - La mayoría de configuraciones provienen del archivo de constantes: config.constantSubViewDICOM, 
            si necesitas entender qué hace cada carecterística revisa el archivo de constantes.
    
    """
    
    def configure_items(self):
        self.ui_text_name.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_ID_Patient.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_date_born.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_sex.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_institution_name.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_study_ID.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_body_part.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_acquisition_test.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_acquisition_time.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_img.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_POSITION_X, consVDcm.DEFAULT_TEXT_POSITION_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        
    
    """
    El método configure_items permite configurar los elementos (items) que conforman a la subinterfaz
    
    """
    
    
    def insert_elements(self):
        #Insertamos la escena en el GraphicsView
        self.ui_graphics_view.insert_element(self.ui_graphics_scene.q_scene)
        
        #Insertamos el GraphicsWidget en el GraphicsScene
        self.ui_graphics_scene.insert_element(self.ui_graphics_widget.q_widget)
        
        #Insertamos todos los elementos necesarios en el GraphicsWidget
        # self.ui_graphics_widget.insert_element([self.ui_layout_main]) #En este caso no se inserta, debido a que el Layout_main será el encargado de tener a todos los elementos
        
        #Insertamos los elementos correspondientes en los layout correspondientes
        self.ui_layout_left.insert_element([self.ui_text_img.q_text_container, self.ui_text_img_now.q_text_container, 
                                            self.ui_text_img_end.q_text_container])
        
        self.ui_layout_right_1.insert_element([self.ui_text_date_born.q_text_container, 
                                               self.ui_text_sex.q_text_container])
        
        self.ui_layout_right_2.insert_element([self.ui_text_acquisition_test.q_text_container, self.ui_text_acquisition_time.q_text_container])
        
        # self.ui_layout_center.insert_element([self.ui_img_dicom.q_pixmap])        
        
        #Por último, insertamos los layout dentro de los QWidget correspondientes
        self.ui_widget_left_1.insert_element(self.ui_layout_left.q_layout)
        self.ui_widget_right_1.insert_element(self.ui_layout_right_1.q_layout)
        self.ui_widget_right_2.insert_element(self.ui_layout_right_2.q_layout)
        self.ui_widget_center.insert_element(self.ui_layout_center.q_layout)
        
        
        #El layout principal es en el que se establecerán todos los elementos, siendo el layout del QGraphicsWidget
        self.ui_layout_main.insert_element(self.define_positions_items())
        
        
    """
    El método insert_elements nos permite poder insertar los elementos necesarios
    en sus respectivos contenedores.
    
    - Inserciones:
        - Graphics_View : En este contenedor insertamos la escena por medio del QGraphicsScene
        - Graphics_Scene: En este contenedor insertamos el Widget por medio del QGraphicsWidget
        - Graphics_Widget: En este contenedor insertamos todos los elementos que conformarán la interfaz.
    """
    
    def define_positions_items(self) -> list[dict]:
        list_positions = list()
        
        list_positions.append({"element": self.ui_widget_left_1.q_widget, 
                                   "row": 1, 
                                   "col": 1, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_widget_center.q_widget, 
                                   "row": 1, 
                                   "col": 2, 
                                   "rows_span": 10, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_text_name.q_text_container, 
                                   "row": 1, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_text_ID_Patient.q_text_container, 
                                   "row": 2, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_widget_right_1.q_widget, 
                                   "row": 3, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_text_institution_name.q_text_container, 
                                   "row": 4, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_text_study_ID.q_text_container, 
                                   "row": 5, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_text_body_part.q_text_container, 
                                   "row": 6, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_text_ID_Patient.q_text_container, 
                                   "row": 2, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_widget_right_2.q_widget,
                                   "row": 10,
                                   "col": 3,
                                   "rows_span": 1,
                                   "col_span": 1
                                   }
                              )
        
        return list_positions