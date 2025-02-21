from abc import ABC, abstractmethod
from core.viewsUI.AbsConnection import AbsConnection 

class AbsMenus(ABC, AbsConnection):
    @abstractmethod
    def create_menu(self):
        pass
    
    @abstractmethod
    def enable_menu(self):
        pass
    
    @abstractmethod
    def disable_menu(self):
        pass
