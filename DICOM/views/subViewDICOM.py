import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from utils.Graphics import GraphicsView, GraphicsScene
from config import constantSubViewDICOM as consVDcm

class subViewDICOM(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.obj_graphics_view  = GraphicsView()
        self.obj_graphics_scene = GraphicsScene()
        
        self.generate_widget()
        self.generate_items()
    
    def generate_widget(self):
        widget_main = QWidget(self)
        layout = QHBoxLayout(widget_main)
        layout.addWidget(self.obj_graphics_view.graphics_view)
        
        self.setCentralWidget(widget_main)
        self.setWindowTitle("SubView DICOM")
    """
    El método permite crear y configurar los items que tendrá la subInterfaz.
    
    - NOTA:
        - La mayoría de configuraciones provienen del archivo de constantes: config.constantSubViewDICOM, 
            si necesitas entender qué hace cada carecterística revisa el archivo de constantes.
    
    """
    def generate_items(self):
        #Configuramos las características del view
        self.obj_graphics_view.configure_features(consVDcm.BACKGROUND_COLOR_DEFAULT, consVDcm.FRAME_STYLE_DEFAULT)
        
        #Configuramos el comportamiento del View
        self.obj_graphics_view.configure_behaivor(consVDcm.DRAG_MODE_DEFAULT, consVDcm.INTERACTIVE_DEFAULT,
                                              consVDcm.RESIZE_ANCHOR_DEFAULT,consVDcm.VIEW_PORT_UPDATE_MODE_DEFAULT)
        
        #Creamos la Escena y la configuramos
        self.obj_graphics_scene.configure_features()