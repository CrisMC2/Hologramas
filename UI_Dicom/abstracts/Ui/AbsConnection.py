from abc import ABC, abstractmethod

class AbsConnection(ABC):
    @abstractmethod
    def connections(self):
        pass