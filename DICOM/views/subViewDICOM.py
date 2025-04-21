#Importamos partes de librerías
from PyQt5.QtWidgets import QApplication, QMainWindow #No eliminar el QApplication, es necesario para el test desde tests.test_subViewDICOM
from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsProxyWidget, QGraphicsPixmapItem, QGraphicsLinearLayout, QLayout
from PyQt5.QtCore import QSize

#Importamos clases del mismo proyecto (Programa nuestro)
from utils.Graphics import GraphicsView, GraphicsScene, GraphicsWidget, GraphicsProxyWidget
from utils.Layout import LinearLayout, GridLayout
from utils.Widgets import Widget
from utils.ElementsWidgets import TextWidget, SliderWidget
from utils.PixmapUi import PixmapUi
from config import constantSubViewDICOM as consVDcm

class Ui_subViewDicom(QMainWindow):
    """
    La interfaz Ui_subViewDicom está diseñada para dotar de una visualización completa
    de un archivo o grupo de archivos DICOM.
    
    - Parámetros:
        - self (Ui_subViewDicom)    : Instancia de la clase Ui_subViewDicom
        - main_container (tuple[QWidget, Qlayout])  : Instancia de un QWidget y un QLayout que permitan la inserción
                                                        del QGraphicsView.
    """
    
    def __init__(self):
        super().__init__()

    def setupSubUi(self, main_container: tuple[QWidget, QLayout]):
        self.generate_containers() #Generamos los contenedores que tendrá la interfaz
        self.generate_items() #Generamos los items que tendrá la interfaz
        
        self.configure_containers() #Configuramos los contenedores que usaremos
        # self.configure_items()
        
        self.insert_elements() #Insertamos los elementos en los contenedores
        
        self.setup_sub_view_dicom(main_container[0], main_container[1])
    
    def generate_containers(self):
        #Contenedores clave para la visualización (lienzo, escena, layout)
        self.ui_graphics_view   = GraphicsView()
        self.ui_graphics_scene  = GraphicsScene()
        self.ui_layout_main = GridLayout(consVDcm.DEFAULT_ROWS_LAYOUT, consVDcm.DEFAULT_COLS_LAYOUT)
        self.ui_graphics_widget = GraphicsWidget(self.ui_layout_main.q_grid_layout)  #Como layout principal configuramos al GridLayout creado anteriormente
       
        #Contenedores para el posicionamiento de los elementos
        self.ui_layout_left = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_1) #Utilizamos la constante del tipo de Layout que tendrá el Widget
        self.ui_layout_right_1 = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_1)
        self.ui_layout_right_2 = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_1)
        self.ui_layout_center = LinearLayout(QGraphicsLinearLayout, consVDcm.DEFAULT_ORIENTATION_LAYOUT_2)
        
        #Contenedores para la inserción de Widgets (Elementos o Items) en las instancias Graphics
        self.ui_proxy_text_name = GraphicsProxyWidget()
        self.ui_proxy_text_ID_Patient = GraphicsProxyWidget()
        self.ui_proxy_text_date_born = GraphicsProxyWidget()
        self.ui_proxy_text_sex = GraphicsProxyWidget()
        self.ui_proxy_text_institution_name = GraphicsProxyWidget()
        self.ui_proxy_text_study_ID = GraphicsProxyWidget()
        self.ui_proxy_text_body_part = GraphicsProxyWidget()
        self.ui_proxy_text_acquisition_test = GraphicsProxyWidget()
        self.ui_proxy_text_acquisition_time = GraphicsProxyWidget()
        self.ui_proxy_text_img = GraphicsProxyWidget()
        self.ui_proxy_text_img_now = GraphicsProxyWidget()
        self.ui_proxy_text_img_end = GraphicsProxyWidget()
        self.ui_proxy_img_dicom = GraphicsProxyWidget()
        
        self.ui_proxy_slider = GraphicsProxyWidget()
        
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
    
    NOTA IMPORTANTE:
        - No confundir GraphicsView, GraphicsScene, GraphicsWidget, GraphicsProxyWidget,
            LinearLayout con las clases propias de PyQt5.
            
            Las clases usadas en este método para la creación de los contenedores son 
            propias del proyecto (Desarrolladas por el equipo)
    """   
    def setup_sub_view_dicom(self, MainWidget: QWidget, MainLayout: QLayout):
        MainLayout.addWidget(self.ui_graphics_view.q_view)
        
        self.setCentralWidget(MainWidget)
        self.setWindowTitle("SubView DICOM")
        
    """
    El método setup_sub_view_dicom de la clase Ui_subViewDicom es el método encargado de insertar 
    toda la vista en un contenedor.
    
    - Parámetros:
        - self (Ui_subViewDicom)    : Instancia de la clase Ui_subViewDicom.
        - MainWidget (QWidget)      : Elemento QWidget encargado de ser el widget central de la vista.
        - MainLayout (QLayout)      : Elemento QLayout encargado de agregar el QGraphicsView; contenedor principal de la vista.
    """ 
    
    def generate_items(self) -> None:
        self.ui_text_img = TextWidget(QLabel()) #Generamos un elemento QWidget
        self.ui_text_img_now = TextWidget(QLabel())
        self.ui_text_img_end = TextWidget(QLabel())       
        self.ui_text_name = TextWidget(QLabel())
        self.ui_text_ID_Patient = TextWidget(QLabel())
        self.ui_text_date_born = TextWidget(QLabel())
        self.ui_text_sex = TextWidget(QLabel())
        self.ui_text_institution_name = TextWidget(QLabel())
        self.ui_text_study_ID = TextWidget(QLabel())
        self.ui_text_body_part = TextWidget(QLabel())
        self.ui_text_acquisition_test = TextWidget(QLabel())
        self.ui_text_acquisition_time = TextWidget(QLabel())
        
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
    
    def configure_containers(self) -> None:
        #Configuramos las características del View
        self.ui_graphics_view.configure_features(consVDcm.SCROLL_BAR_POLICY_DEFAULT, consVDcm.BACKGROUND_COLOR_DEFAULT, consVDcm.FRAME_STYLE_DEFAULT)
        
        #Configuramos el comportamiento del View
        self.ui_graphics_view.configure_behaivor(consVDcm.SIZE_POLICY_DEFAULT, consVDcm.DRAG_MODE_DEFAULT, consVDcm.INTERACTIVE_DEFAULT,
                                              consVDcm.RESIZE_ANCHOR_DEFAULT,consVDcm.VIEW_PORT_UPDATE_MODE_DEFAULT)
        
        #Configuramos las características de la Scene
        self.ui_graphics_scene.configure_features((600,500), consVDcm.SCENE_RECT_DEFAULT, consVDcm.BACKGROUND_COLOR_DEFAULT_2)
        
        #Configuramos el comportamiento de la Scene
        self.ui_graphics_scene.configure_behaivor(consVDcm.ITEM_INDEX_METHOD_DEFAULT)
         
        #Configuramos las características del GraphicsWidget
        self.ui_graphics_widget.configure_features(self.ui_graphics_scene.q_scene)
        
        #Configuramos el comportamiento del GraphicsWidget
        self.ui_graphics_widget.configure_behaivor(consVDcm.SIZE_POLICY_DEFAULT)  
        
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
                
    """
    El método permite configurar los containers que tendrá la subInterfaz.
    
    - NOTA:
        - La mayoría de configuraciones provienen del archivo de constantes: config.constantSubViewDICOM, 
            si necesitas entender qué hace cada carecterística revisa el archivo de constantes.
    
    """
    
    def configure_items(self) -> None:
        self.ui_text_name.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_ID_Patient.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_date_born.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_sex.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_institution_name.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_study_ID.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_body_part.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_acquisition_test.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_acquisition_time.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        self.ui_text_img.configure_features(consVDcm.DEFAULT_TEXT_FONT,
                                             consVDcm.DEFAULT_TEXT_SIZE_X, consVDcm.DEFAULT_TEXT_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_X, consVDcm.DEFAULT_TEXT_MINIMUM_SIZE_Y,
                                             consVDcm.DEFAULT_TEXT_SIZE_POLICY_X,consVDcm.DEFAULT_TEXT_SIZE_POLICY_Y,
                                             consVDcm.DEFAULT_TEXT_BACKGROUND_COLOR, consVDcm.DEFAULT_TEXT_COLOR)
        
    """
    El método configure_items permite configurar los elementos (items) que conforman a la subinterfaz
    
    """
    
    
    def insert_elements(self) -> None:
        #Insertamos la escena en el GraphicsView
        self.ui_graphics_view.insert_element(self.ui_graphics_scene.q_scene)
        
        #Insertamos el GraphicsWidget en el GraphicsScene
        self.ui_graphics_scene.insert_element(self.ui_graphics_widget.q_widget)
        
        #Insertamos todos los elementos necesarios en el GraphicsWidget
        # self.ui_graphics_widget.insert_element([self.ui_layout_main]) #En este caso no se inserta, debido a que el Layout_main será el encargado de tener a todos los elementos
        
        #Insertamos los elementos "Q" en sus respectivos QGraphicsProxyWidget
        self.ui_proxy_text_name.insert_element(self.ui_text_name.q_text)
        self.ui_proxy_text_ID_Patient.insert_element(self.ui_text_ID_Patient.q_text)
        self.ui_proxy_text_date_born.insert_element(self.ui_text_date_born.q_text)
        self.ui_proxy_text_sex.insert_element(self.ui_text_sex.q_text)
        self.ui_proxy_text_institution_name.insert_element(self.ui_text_institution_name.q_text)
        self.ui_proxy_text_study_ID.insert_element(self.ui_text_study_ID.q_text)
        self.ui_proxy_text_body_part.insert_element(self.ui_text_body_part.q_text)
        self.ui_proxy_text_acquisition_test.insert_element(self.ui_text_acquisition_test.q_text)
        self.ui_proxy_text_acquisition_time.insert_element(self.ui_text_acquisition_time.q_text)
        self.ui_proxy_text_img.insert_element(self.ui_text_img.q_text)
        self.ui_proxy_text_img_now.insert_element(self.ui_text_img_now.q_text)
        self.ui_proxy_text_img_end.insert_element(self.ui_text_img_end.q_text)
        
        self.ui_proxy_slider.insert_element(self.ui_slider.q_slider)
        
        self.ui_proxy_img_dicom.insert_element(self.ui_img_dicom.q_pixmap)
        
        #Insertamos los elementos correspondientes en los layout correspondientes
        self.ui_layout_left.insert_element([self.ui_proxy_text_img.q_proxy_widget, self.ui_proxy_text_img_now.q_proxy_widget, 
                                            self.ui_proxy_text_img_end.q_proxy_widget])
        
        self.ui_layout_right_1.insert_element([self.ui_proxy_text_date_born.q_proxy_widget, 
                                               self.ui_proxy_text_sex.q_proxy_widget])
        
        self.ui_layout_right_2.insert_element([self.ui_proxy_text_acquisition_test.q_proxy_widget, 
                                               self.ui_proxy_text_acquisition_time.q_proxy_widget])
        
        self.ui_layout_center.insert_element([self.ui_proxy_img_dicom.q_proxy_widget])
        # self.ui_layout_center.insert_element([self.ui_img_dicom.q_pixmap])                
        
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
        
        list_positions.append({"element": self.ui_layout_left.q_layout, 
                                   "row": 1, 
                                   "col": 1, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_layout_center.q_layout, 
                                   "row": 1, 
                                   "col": 2, 
                                   "rows_span": 10, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_proxy_text_name.q_proxy_widget, 
                                   "row": 1, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_proxy_text_ID_Patient.q_proxy_widget, 
                                   "row": 2, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_layout_right_1.q_layout, 
                                   "row": 3, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_proxy_text_institution_name.q_proxy_widget, 
                                   "row": 4, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_proxy_text_study_ID.q_proxy_widget, 
                                   "row": 5, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_proxy_text_body_part.q_proxy_widget, 
                                   "row": 6, 
                                   "col": 3, 
                                   "rows_span": 1, 
                                   "col_span": 1})
                              
        list_positions.append({"element": self.ui_layout_right_2.q_layout,
                                   "row": 10,
                                   "col": 3,
                                   "rows_span": 1,
                                   "col_span": 1
                                   })
        
        list_positions.append({"element": self.ui_proxy_slider.q_proxy_widget,
                                    "row": 1,
                                    "col": 4,
                                    "rows_span": 10,
                                    "cols_span": 1
                                    })
        
        return list_positions