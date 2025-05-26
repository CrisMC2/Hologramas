from abc import abstractmethod

#Importancias de clases del proyecto
from abstracts.Ui.AbsWidget import AbsWidget

class AbsTextControl(AbsWidget):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_data(self) -> str:
        pass
    
    @abstractmethod
    def change_data(self, new_data: str):
        pass