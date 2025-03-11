import numpy as np

from PyQt5.QtWidgets import QMenu, QAction, QStackedWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap

from core.viewsUI.AbsMenus import AbsMenus
from core.viewsUI.AbsActions import AbsActions
from core.viewsUI.AbsResourceUI import AbsPixmap 
from utils.ViewDicom import ViewAxial, ViewCoronal, ViewSagittal

class SelectCantViews(AbsMenus, AbsActions):
    def __init__(self, cant_view_default: int):
        super().__init__()
        self.cant_view_default = cant_view_default
    
    #Herencia de AbsMenus
    def create_menu(self):
        menu_cant_views = QMenu()
        self.create_actions()
        self.check_action(self.list_actions)
        
        menu_cant_views.addActions(self.list_actions)
        return menu_cant_views

    #Herencia de AbsActions
    def create_actions(self):
        self.one_view = QAction("1 View", self)
        self.two_view = QAction("2 Views", self)
        self.four_view = QAction("4 Views", self)
        
        self.list_actions = [self.one_view, self.two_view, self.four_view]
    
    #Herencia de AbsActions -> AbsConnections
    def connections(self):        
        self.one_view.triggered.connect(lambda : self.toggle_check_action(self.one_view, self.list_actions))
        self.two_view.triggered.connect(lambda : self.toggle_check_action(self.two_view, self.list_actions))
        self.four_view.triggered.connect(lambda : self.toggle_check_action(self.four_view, self.list_actions))
    
    #Herencia de AbsMenus
    def enable_menu(self, enable, menu):
        super().enable_menu(enable, menu)
    
    #Herencia de AbsActions
    def check_action(self, list_actions: list[QAction]):
        for action in list_actions:
            action.setCheckable(True)
    
    #Herencia de AbsActions
    def toggle_check_action(self, action: QAction, list_actions: list [QAction]):
        super().toggle_check_action(action, list_actions)
        
        
        
        
            
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