#Importamos parte de una librería
from abc import ABC, abstractmethod

#Importamos una clase del mismo proyecto
from abstracts.Ui.AbsContainers import AbsContainers


class AbsLayout(AbsContainers):
    """
    La clase AbsLayout está pensada para ser una plantilla
    que englobe las funciones más características y relevantes 
    que se necesitarán para la interacción con los Layout.
    
    - Herencia:
        - @class AbsContainers      : Clase abstracta base para contenedores.
    
    - Métodos:
        - @abstractmethod create_layout(self, type_layout)     : Método propio de AbsLayout
                                                                    diseñado para la futura creación del Layout.
                                                                    
        - @abstractmethod configure_features    : Método heredado de AbsContainers
        - @abstractmethod configure_behaivor    : Método heredado de AbsContainers
        - @abstractmethod insert_element        : Método heredado de AbsContainers
    
    """
    
    @abstractmethod
    def create_layout(self, *args, **kwargs):
        pass
    
    """
    El método create_layout cumple la función de definir un layout.
    
    """