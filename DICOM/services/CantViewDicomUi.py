import numpy as np

from PyQt5.QtWidgets import QMenu, QAction

from abstracts.Ui.AbsMenus import AbsMenus

class SelectCantViews(AbsMenus):
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
        self.one_view = QAction("1 View")
        self.two_view = QAction("2 Views")
        self.four_view = QAction("4 Views")
        
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
        
    def emit_signal(self, *args, **kwargs):
        return super().emit_signal(*args, **kwargs)