from abc import ABC, abstractmethod
from DICOM.abstracts.Ui.AbsConnection import AbsConnection 
from PyQt5.QtWidgets import QMenu
class AbsMenus(ABC):
    @abstractmethod
    def create_menu(self):
        pass
    
    """
    La siguiente función permite habilitar ("enable") o deshabilitar ("disable")
    un menú.

    El método funciona de la siguiente manera:
        Si damos true : enabled
        Si damos false: disabled
        
    - Parámetros:
        - enable (bool)         : Variable que define si deseas habilitar o no un menú.
        - menu (QMenu)          : Menú el cual se habilitará o no.
    
    """ 
    def enable_menu(self, enable: bool, menu: QMenu):
        menu.setEnabled(enable)
        
