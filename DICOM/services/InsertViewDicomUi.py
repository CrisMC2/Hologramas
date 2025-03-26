import numpy as np

from PyQt5.QtWidgets import QMenu, QAction, QStackedWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap

from DICOM.abstracts.Ui.AbsMenus import AbsMenus
from DICOM.abstracts.Ui.AbsActions import AbsActions
from DICOM.abstracts.Ui.AbsPixmap import AbsPixmap 
from DICOM.core.classes.DicomView import ViewAxial, ViewCoronal, ViewSagittal  

class InsertView(AbsPixmap):
    def __init__(self, q_graphics_scene):
        self.axial = ViewAxial()
        self.saggital = ViewSagittal()
        self.coronal = ViewCoronal()
        
    def insert_view(self, view: str = "Axial View"):
        if view == "Axial View":
            # img_array = self.axial.
            pass
        
        elif view == "Saggital View":
            pass
        elif view == "Coronal View":
            pass