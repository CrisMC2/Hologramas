import numpy as np

from PyQt5.QtWidgets import QMenu, QAction, QStackedWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap

from DICOM.abstracts.Ui.AbsMenus import AbsMenus
from DICOM.abstracts.Ui.AbsActions import AbsActions
from DICOM.abstracts.Ui.AbsPixmap import AbsPixmap 
from DICOM.core.classes.DicomView import ViewAxial, ViewCoronal, ViewSagittal  
            
class SelectView(AbsMenus, AbsActions):
    def __init__(self, view_default: str):
        super().__init__()
        self.view_default = view_default
        
    #Herencia de AbsMenus
    def create_menu(self):
        menuViews = QMenu()
        self.create_actions()
        self.check_action(self.list_actions)
                
        menuViews.addActions(self.list_actions)
        
        return menuViews
    
    #Herencia de AbsActions
    def create_actions(self):
        self.action_AxialView = QAction("Axial View", self)
        self.action_SaggitalView = QAction("Saggital View", self)
        self.action_CoronalView = QAction("Coronal View", self)
        
        self.list_actions = [self.action_AxialView,  self.action_SaggitalView, self.action_CoronalView]
    
    #Herencia de AbsMenus
    def connections(self):
        self.action_AxialView.triggered.connect(lambda : self.toggle_check_action(self.action_AxialView, self.list_actions))
        self.action_SaggitalView.triggered.connect(lambda : self.toggle_check_action(self.action_SaggitalView, self.list_actions))
        self.action_CoronalView.triggered.connect(lambda : self.toggle_check_action(self.action_CoronalView, self.list_actions))
    
    #Herencia de AbsActions
    def check_action(self, list_actions):
        for act in list_actions:
            act.setCheckable(True)

    #Herencia de AbsActions
    def toggle_check_action(self, action: QAction, list_actions: list[QAction]):
        super().toggle_check_action(action, list_actions) 