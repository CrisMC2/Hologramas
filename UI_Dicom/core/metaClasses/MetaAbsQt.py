from abc import ABCMeta
from PyQt5.QtWidgets import QWidget

class MetaAbsQt(ABCMeta, type(QWidget)):
    """Metaclase combinada  para evitar conflictos entre ABC y Qt"""
    pass