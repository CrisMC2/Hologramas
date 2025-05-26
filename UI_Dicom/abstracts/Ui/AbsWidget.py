from abc import ABC, abstractmethod

class AbsWidget(ABC):
    """
    La clase abstracta "AbsWidget" está diseñada para poder dotar 
    de métodos base a los distintos Widgets (Elementos de UI) que puedan usarse
    con librerías como PyQt5, PySide6, TKinter y demás.
    
    - Herencia:
        - @class ABC       : Parte de la librería abc, utilizada para hacer a una clase, abstracta.
    
    - Métodos abstractos
        - @abstractmethod configure_features(self, *args, **kwargs)    : Método propio de la clase AbsWidget para
                                                    la futura configuración y/o definición de características de los widgets.
                                                    
        - @abstractmethod configure_behaivor(self, *args, **kwargs)    : Método propio de la clase AbsWidget para
                                                    la futura configuración y/o definición del comportamiento de los widgets.

    - Nota:
        - *args permite a las implementaciones de los métodos poder definir múltiples parámetros sin nombre o sin valor default (nombre: str, edad: int).
        - **kwargs permite a las implementaciones de los métodos poder definir múltiples parámetros con nombre o valor default (nombre: str = "Ricardo", edad: int = 20).
    """
    
    @abstractmethod
    def configure_features(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def configure_behavior(self, *args, **kwargs):
        pass
    