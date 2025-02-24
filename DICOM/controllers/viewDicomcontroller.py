import sys
import os

uiDicom = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(uiDicom)

#QApplication se utiliza en el test
from PyQt5.QtWidgets import QApplication, QMainWindow
from views.viewDICOM  import Ui_viewDICOM

from services.UploadFiles import MenuUploadFiles

class Ui_DicomController(Ui_viewDICOM, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewDICOM()
        self.ui.setupUi(self)
    
        self.menu()
        
    def menu(self):
        self.menu_upload = MenuUploadFiles(type_file_filter="Dicom (*dcm)", keep_directory_initial=False)
        _menu_upload = self.menu_upload.create_menu()
        _menu_upload.setDisabled(False)
        self.ui.UploadFiles.setMenu(_menu_upload)