import sys
import os

uiDicom = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(uiDicom)

from PyQt5.QtWidgets import QMainWindow

from views.viewDICOM  import Ui_viewDICOM

class Ui_DicomController(Ui_viewDICOM, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_viewDICOM()
        self.ui.setupUi(self)
        
    