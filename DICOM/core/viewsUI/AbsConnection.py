from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QAction

class AbsConnection():
    @abstractmethod
    def connections(self):
        pass