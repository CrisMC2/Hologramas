import sys
import os

uiDicom = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(uiDicom)

from typing import List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget #QApplication se utiliza en el test, NO ELIMINAR
from views.viewDICOM  import Ui_viewDicom
from controllers.subViewDicomController import Ui_subViewDicomController

from services.UploadFilesUi import MenuUploadFiles
from services.CantViewDicomUi import SelectCantViews
from services.SelectViewDicomUi import SelectView

from config import constantViewDICOM as consVDcm
from config import constantSubViewDICOM as consSubVdcm

class Ui_viewDicomController():
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewDicom()
        self.widget_main = QWidget()
        
        self.ui.setupUi(self.widget_main)
        self.setupUiController()
        
    def setupUiController(self):
        self.subUi = Ui_subViewDicomController(self.ui.OneView_Widget, 
                                               self.ui.OneView_Layout)
        self.menus()
        self.connect_signals_menus()
        self.connect_signals_views()

    def menus(self):
        #Menú para subir archivos
        self.__obj_menu_upload = MenuUploadFiles(directory_search_default=consVDcm.DIRECTORY_SEARCH_DEFAULT, type_file_filter=consVDcm.FILTER_SEARCH, 
                                                 keep_directory_default=consVDcm.KEEP_DIRECTORY_DEFAULT) #Utilizamos los valores por defecto o constantes
        self._menu_upload = self.__obj_menu_upload.create_menu()
        self.__obj_menu_upload.enable_menu(True, self._menu_upload)
        self.ui.UploadFiles.setMenu(self._menu_upload)
        
        #Menú para seleccionar cantidad de vistas
        self.__obj_menu_cant_view = SelectCantViews(consSubVdcm.DEFAULT_CANT_VIEWS_DICOM) #Utilizamos los valores por defecto o constantes
        self._menu_cant_view = self.__obj_menu_cant_view.create_menu()
        self.__obj_menu_cant_view.enable_menu(False, self._menu_cant_view)
        self.ui.CantViews.setMenu(self._menu_cant_view)
        
        #Menú para seleccionar la vista
        self.__obj_menu_view = SelectView(consSubVdcm.DEFAULT_VIEW_DICOM) #Utilizamos los valores por defecto o constantes
        self._menu_view = self.__obj_menu_view.create_menu()
        self.__obj_menu_view.enable_menu(False, self._menu_view)
        self.ui.SelectView.setMenu(self._menu_view)

    """
    En esta parte definimos los menus.
    
    Cabe señalar que en cada objeto se instancia la clase padre.
    Luego se crea el menú directamente.
    Se utiliza la instancia de la clase padre para configurar el menú
    Por último se setea el menú en la interfaz
    """
    
    def connect_signals_menus(self):
        self.__obj_menu_upload.obj_signal.connect(self.subUi.setupUiController)
        self.__obj_menu_view.obj_signal.connect(self.subUi.switch_view)
        #self.__obj_menu_cant_view.connect(self.__obj_menu_view.recept_signal)
    
    def connect_signals_views(self):
        self.subUi.obj_emit.obj_signal.connect(self.activate_menus)

    def activate_menus(self, activate: bool = False):
        if activate:
            self.__obj_menu_cant_view.enable_menu(True, self._menu_cant_view)
            self.__obj_menu_view.enable_menu(True, self._menu_view)
        
        self.ui.StackedViews.setCurrentIndex(1)
    """
    El método activate_menu, propio de la clase Ui_viewDicomController permite
    activar los menús que inicialmente se plantean como desactivados.

    - Este método se activa después de que la subViewDicom confirme que la interfaz 
        se mostró con normalidad.
    - Mostrarse con normalidad significa que la carpeta seleccionada para visualizar los 
        DICOMS efectivamente haya tenido elementos DICOM dentro.

    - Estado de los Menús inicialmente:
        - self._menu_upload     : Activated
        - self._menu_cant_view  : Desactivaded
        - self._menu_view       : Desactivaded
    """