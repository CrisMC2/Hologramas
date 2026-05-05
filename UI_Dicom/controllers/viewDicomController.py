import sys
import os

uiDicom = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(uiDicom)

from typing import List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget #QApplication se utiliza en el test, NO ELIMINAR
from UI_Dicom.views.viewDICOM  import Ui_viewDicom
from UI_Dicom.controllers.subViewDicomController import Ui_subViewDicomController

from UI_Dicom.services.UploadFilesUi import MenuUploadFiles
from UI_Dicom.services.CantViewDicomUi import SelectCantViews
from UI_Dicom.services.SelectViewDicomUi import SelectView

from UI_Dicom.config import constantViewDICOM as consVDcm
from UI_Dicom.config import constantSubViewDICOM as consSubVdcm

#=============================================
#Importamos clases/Métodos/Elementos de otros Monolitos
from Modeling_3D.main import Execute_Modeling3D

class Ui_viewDicomController():
    def __init__(self):
        super().__init__()
        
        #=========Define la estructura de la vista principal=============
        self.ui = Ui_viewDicom()
        self.widget_main = QWidget()
        self.ui.setupUi(self.widget_main)
        
        #=========Define la relación de los elementos de la vista principal=============
        self.setupUiController()
        
    def setupUiController(self):
        #=========Define la estructura de la vista secundaria=============
        self.subUi = Ui_subViewDicomController(self.ui.OneView, 
                                               self.ui.OneView_Layout)
        
        # Define la lógica de los menús
        self.menus() #Define
        self.connect_signals_menus() #Conecta las señales
        self.connect_signals_views() #Conecta la señal a la vista
        self.disconnect_links()
        
        #=========Define la lógica de la interfaz secundaria=============
        self.modeling_3D = Execute_Modeling3D()


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
        self.__obj_menu_upload.obj_signal.connect(self.subUi.setupUiController) # envía un string (path)
        self.__obj_menu_view.obj_signal.connect(self.subUi.switch_view) # envía un string (name view)
        #self.__obj_menu_cant_view.connect(self.__obj_menu_view.recept_signal)
    
    """
    Se utiliza la señal del Controlador de la subInterfaz para habilitar los demás menús que provee la interfaz principal.
    
    Lógica Interna:
        - If (signal - subviewController) : true => Se activan los demás menús, Se activan las vistas del StackView
    """
    def connect_signals_views(self):
        self.subUi.obj_emit.obj_signal.connect(self.activate_menus)
        self.subUi.obj_emit.obj_signal.connect(self.activate_view)
    
    def disconnect_links(self):
        try:
            self.ui.pushButton.clicked.disconnect() 
        except TypeError:
            pass

    def activate_menus(self, activate: bool = False):
        self.__obj_menu_cant_view.enable_menu(activate, self._menu_cant_view)
        self.__obj_menu_view.enable_menu(activate, self._menu_view)
        
    
    """
    El método permite mostrar las vistas del stackView, conjunto a conectar el botón del STl con el método de la vista tridimensional (Revisar Modeling3.main)
    """
    def activate_view(self, activate: bool = False):
        self.ui.StackedViews.setCurrentIndex(1)

        if (activate):
            print("Ejecución activates_view")
            # Conectamos a la siguiente interfaz
            self.ui.pushButton.clicked.connect(lambda: self.modeling_3D.execute(self.subUi.dicom_list[200:])) # Limitamos la cantidad para solo renderizar la columna lumbar
        
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