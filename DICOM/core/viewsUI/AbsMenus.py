from abc import ABC, abstractmethod
from core.viewsUI.AbsConnection import AbsConnection 
from PyQt5.QtWidgets import QMenu
class AbsMenus(ABC):
    @abstractmethod
    def create_menu(self):
        pass
    
    @abstractmethod
    def enable_menu(self, enable: bool, menu: QMenu):
        pass
