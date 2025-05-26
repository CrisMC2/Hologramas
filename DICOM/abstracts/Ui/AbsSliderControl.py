from abc import ABC, abstractmethod

class AbsSliderControl(ABC):    
    # @abstractmethod
    # def create_slider(self):
    #     pass
    @abstractmethod
    def show_slider(self, show: bool):
        pass
    
    @abstractmethod
    def define_range(self, start: int, end: int):
        pass
    
    @abstractmethod
    def set_value(self, new_value: int):
        pass
    
    @abstractmethod
    def get_value(self) -> int:
        pass
    
    @abstractmethod
    def get_value_edit(self, difference: int) -> int:
        pass