from abc import ABC, abstractmethod

#Importamos la clase AbsConnection de la siguiente manera debido a que luego para 
#   su utilizaciòn es necesario que provenga de una carpeta "superior" (Que no tenga profundidad)
from abstracts.Ui.AbsActions import AbsActions
from abstracts.classes.AbsSignal import AbsEmisor
from PyQt5.QtWidgets import QMenu

class AbsMenus(AbsActions, AbsEmisor):
    @abstractmethod
    def create_menu(self):
        pass
    
    def enable_menu(self, enable: bool, menu: QMenu):
        menu.setEnabled(enable)

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