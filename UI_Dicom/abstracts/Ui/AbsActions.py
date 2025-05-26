from abc import abstractmethod

from PyQt5.QtWidgets import QAction, QWidget
# from PyQt5.QtCore import QObject 
from abstracts.Ui.AbsConnection import AbsConnection
from core.metaClasses.MetaAbsQt import MetaAbsQt

#Absconnection ya es abstracta (hereda de ABC), por lo que no hace falta ponerlo de nuevo
class AbsActions(AbsConnection, QWidget, metaclass=MetaAbsQt):
    """Cuando generes una instancia de la clase no olvides la línea de 
            super().__init__() 
        para que todo funcione bien"""
    
    @abstractmethod
    def create_actions(self):
        pass
    """
    El método create_actions permite crear las acciones que sean necesarias.
    """

    @abstractmethod
    def check_action(self, list_actions: list[QAction]):
        pass
    """
    El método check_action de la clase AbsActions
    está pensado para poder "checkear" una lista de acciones.
    
    setCheckable => Esto permite darle a una acción un estado de selección
    """

    def toggle_check_action(self, action: QAction, list_actions: list[QAction]):
        for act in list_actions:
            if act.isCheckable():
                act.setChecked(act == action) #De esta manera solo será True si la acción es igual.                   
    """
    El método está pensado para alternar la única acción que sea "checked"
    dentro de una lista de QAction
    
    - setChecked(True)  => La acción está seleccionada.
    - setChecked(False) => La acción no está seleccionada.
    
    - Parámetros:
        - self (AbsActions)             : Instancia de la clase AbsActions
        - action (QAction)              : Instancia de la clase QAction que será checkeada
        - list_action (list[QAction])   : Lista de QAction las cuales dependiendo de si es la acción exclusiva o no serán set.checked(False)
    """

#Esta clase debería separarse si la lógica llega a extenderse más allá de solo los checked


# class AbsControllerActions():    
    # """
    # El método está pensado para poder "checkear" una lista de acciones.
    
    # setCheckable => Esto permite darle a una acción un estado de selección
    # """
    # @abstractmethod
    # def check_action(self, list_actions: list[QAction]):
    #     pass
    
    # """
    # El método está pensado para alternar la única acción que sea "checked"
    # dentro de una lista de QAction
    
    # - setChecked(True)  => La acción está seleccionada.
    # - setChecked(False) => La acción no está seleccionada.
    
    # - Parámetros:
    #     - self (AbsActions)             : Instancia de la clase AbsActions
    #     - action (QAction)              : Instancia de la clase QAction que será checkeada
    #     - list_action (list[QAction])   : Lista de QAction las cuales dependiendo de si es la acción exclusiva o no serán set.checked(False)
    # """
    
    # def toggle_check_action(self, action: QAction, list_actions: list[QAction]):
    #     for act in list_actions:
    #         if not act.isCheckable():
    #             act.setCheckable(True)
            
    #         if action == act:
    #             act.setChecked(True)
    #         else:
    #             act.setChecked(False)
                