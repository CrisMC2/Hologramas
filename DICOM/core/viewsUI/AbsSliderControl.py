from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QSlider

class AbsSliderControl(ABC):
    """
    Al heredar la clase no olvides agregar al constructor de la clase hija:
    
    - super().__init__(qslider_clase_hija)
    
    Esto hará que la clase padre pueda trabajar con la instancia que necesita.
    """
    def __init__(self, qslider: QSlider):
        self.slider = qslider
    
    # @abstractmethod
    # def create_slider(self):
    #     pass

    @abstractmethod
    def define_range(self, start: int, end: int):
        pass
    
    @abstractmethod
    def show_slider(self, show: bool):
        pass
    
    @abstractmethod
    def get_value(self) -> int:
        pass
    
    @abstractmethod
    def get_value_edit(self, difference: int) -> int:
        pass