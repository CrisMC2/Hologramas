from abc import ABC, abstractmethod

#Importamos la clase AbsConnection de la siguiente manera debido a que luego para 
#   su utilizaciòn es necesario que provenga de una carpeta "superior" (Que no tenga profundidad)
from UI_Dicom.abstracts.Ui.AbsActions import AbsActions
from Shared.abstracts.AbsSignal import AbsEmisor
from PyQt5.QtWidgets import QMenu

class AbsMenus(AbsEmisor, AbsActions):
    """
    La clase AbsMenus regula la estructura y comportamiento que tendrán los menús en la interfaz
    
    - Herencia:
        - AbsEmisor (QWidget, ABC)      : Clase abstracta que regula el comportamiento de las señales
        - AbsActions (ABC, QWidget)     : Clase abstracta que regula el comportamiento de las acciones
    
    Nota =>
        Es vital que el orden de la herencia se realice de esta manera: AbsEmisor, AbsActions
            Esto se debe a que al hacer la herencia de esta manera, el MRO toma de clase padre o metaclase primero 
            a QWidget, lo cual es vital para que las señales, que heredan de QObject, se inicialicen de manera correcta.
            
            Si no se hace en este orden habrá un error con las señales
    """
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