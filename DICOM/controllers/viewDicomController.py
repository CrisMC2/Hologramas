import sys
import os

uiDicom = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(uiDicom)

from typing import List

from PyQt5.QtWidgets import QApplication, QMainWindow #QApplication se utiliza en el test, NO ELIMINAR
from views.viewDICOM  import Ui_viewDICOM
from controllers.subViewDICOM import Ui_subViewDicom

from services.UploadFilesUi import MenuUploadFiles
from services.CantViewDicomUi import SelectCantViews
from services.SelectViewDicomUi import SelectView
from utils.SignalData import Receptor_text, Receptor_list

from config import constantViewDICOM as consVDcm

class Ui_viewDicomController(Ui_viewDICOM, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewDICOM()
        self.ui.setupUi(self)

        self.subUi = Ui_subViewDicom(self.ui.)
    
        self.menu()
    
    """
    En esta parte definimos los menus.
    
    Cabe señalar que en cada objeto se instancia la clase padre.
    Luego se crea el menú directamente.
    Se utiliza la instancia de la clase padre para configurar el menú
    Por último se setea el menú en la interfaz
    """
    def menus(self):
        #Menú para subir archivos
        self.__obj_menu_upload = MenuUploadFiles(directory_search_default=consVDcm.DIRECTORY_SEARCH_DEFAULT, type_file_filter=consVDcm.FILTER_SEARCH, 
                                                 keep_directory_default=consVDcm.KEEP_DIRECTORY_DEFAULT) #Utilizamos los valores por defecto o constantes
        self._menu_upload = self.__obj_menu_upload.create_menu()
        self.__obj_menu_upload.enable_menu(True, self._menu_upload)
        self.ui.UploadFiles.setMenu(self._menu_upload)
        
        #Menú para seleccionar cantidad de vistas
        self.__obj_menu_cant_view = SelectCantViews(consVDcm.CANT_VIEWS_DICOM_DEFAULT) #Utilizamos los valores por defecto o constantes
        self._menu_cant_view = self.__obj_menu_cant_view.create_menu()
        self.__obj_menu_cant_view.enable_menu(False, self._menu_cant_view)
        self.ui.CantViews.setMenu(self._menu_cant_view)
        
        #Menú para seleccionar la vista
        self.__obj_menu_view = SelectView(consVDcm.VIEW_DICOM_DEFAULT) #Utilizamos los valores por defecto o constantes
        self._menu_view = self.__obj_menu_view.create_menu()
        self.__obj_menu_view.enable_menu(False, self._menu_view)
        self.ui.SelectView.setMenu(self._menu_view)

    def connect_signals_menus(self):
        self.__obj_menu_upload.connect(self.subUi.setupUi)
        self.__obj_menu_view.connect(self.subUi.setupUi)
        #self.__obj_menu_cant_view.connect(self.__obj_menu_view.recept_signal)
       
    def activate_menus(self):
        self.__obj_menu_cant_view.enable_menu(True, self._menu_cant_view)
        self.__obj_menu_view.enable_menu(True, self._menu_view)
    
    """
    El método activate_menu, propio de la clase Ui_viewDicomController permite
    activar los menús que inicialmente se plantean como desactivados.
    
    - Estado de los Menús inicialmente:
        - self._menu_upload     : Activated
        - self._menu_cant_view  : Desactivaded
        - self._menu_view       : Desactivaded
    """