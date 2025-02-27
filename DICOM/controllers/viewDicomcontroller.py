import sys
import os

uiDicom = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(uiDicom)

from PyQt5.QtWidgets import QApplication, QMainWindow #QApplication se utiliza en el test, NO ELIMINAR
from views.viewDICOM  import Ui_viewDICOM

from services.UploadFilesUI import MenuUploadFiles
from services.SetViewDicomUI import SelectCantViews, SelectView
from config import constantViewDICOM as consVDcm

class Ui_DicomController(Ui_viewDICOM, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewDICOM()
        self.ui.setupUi(self)
    
        self.menu()
    
    """
    En esta parte definimos los menus.
    
    Cabe señalar que en cada objeto se instancia la clase padre.
    Luego se crea el menú directamente.
    Se utiliza la instancia de la clase padre para configurar el menú
    Por último se setea el menú en la interfaz
    """
    def menu(self):
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
    
    def activate_dicom(self):
        self.__obj_menu_cant_view.enable_menu(True, self._menu_cant_view)
        self.__obj_menu_view.enable_menu(True, self._menu_view)