import numpy as np

from PyQt5.QtWidgets import QMenu, QAction

from abstracts.Ui.AbsMenus import AbsMenus
from config import constantViewDICOM as consVDcm 

class SelectView(AbsMenus):
    def __init__(self, view_default: str):
        super().__init__()
        self.view_default = view_default
        
    #Herencia de AbsMenus
    def create_menu(self):
        menuViews = QMenu()
        self.create_actions()
        self.check_action(self.list_actions)
        self.connections()
        
        menuViews.addActions(self.list_actions)
        
        return menuViews
    
    #Herencia de AbsActions
    def create_actions(self):
        self.action_AxialView = QAction(consVDcm.VIEWS_DICOM[0])
        self.action_SaggitalView = QAction(consVDcm.VIEWS_DICOM[1])
        self.action_CoronalView = QAction(consVDcm.VIEWS_DICOM[2])
        
        self.list_actions = [self.action_AxialView,  self.action_SaggitalView, self.action_CoronalView]
    
    #Herencia de AbsMenus
    def connections(self):
        self.action_AxialView.triggered.connect(lambda : self.toggle_check_action(self.action_AxialView, self.list_actions))
        self.action_SaggitalView.triggered.connect(lambda : self.toggle_check_action(self.action_SaggitalView, self.list_actions))
        self.action_CoronalView.triggered.connect(lambda : self.toggle_check_action(self.action_CoronalView, self.list_actions))
        
        self.action_AxialView.triggered.connect(lambda : self.emit_signal(self.action_AxialView))
        self.action_SaggitalView.triggered.connect(lambda : self.emit_signal(self.action_SaggitalView))
        self.action_CoronalView.triggered.connect(lambda : self.emit_signal(self.action_CoronalView))

    def enable_menu(self, enable, menu):
        return super().enable_menu(enable, menu)
    
    #Herencia de AbsActions
    def check_action(self, list_actions):
        for act in list_actions:
            act.setCheckable(True)

    #Herencia de AbsActions
    def toggle_check_action(self, action: QAction, list_actions: list[QAction]):
        super().toggle_check_action(action, list_actions) 

    #Herencia de AbsEmisor
    def emit_signal(self, signal: QAction):
        self.obj_signal.emit(signal.text())