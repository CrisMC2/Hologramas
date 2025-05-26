from abc import abstractmethod
from abstracts.Ui.AbsWidget import AbsWidget #Abstracción Principal (DICOM.abstracts.Ui.AbsWidget)

class AbsContainers(AbsWidget):
    """
    La clase abstracta "AbsContainers" está diseñada con la intención de permitir 
    dar una serie de características escenciales a los distintos contenedores
    que pueden implementarse con distintas librerías como PyQt5, PySide6, TKinter y demás.
    
    - Herencia:
        - Clase Abstracta "AbsWidget(ABC)" : Especializada en las características de los distintos Widgets
    
    - Métodos Abstractos:
        - @abstractmethod insert_element(self, *args, **kwargs) : Método propio de la clase AbsContainers para 
                                                                    la futura inserción de elementos en los contenedores.
    """
    
    @abstractmethod
    def insert_element(self, *args, **kwargs):
        pass
    """
    El método abstracto "insert_element" de la clase abstracta AbsContainers
    está pensado para insertar elementos dentro del contenedor que se defina.
    
    - Parámetros:
        - self (AbsContainers)      : Instancia de la clase AbsContainers
        - *args                     : "Argumentos Posicionales Variables", necesario para que las instancias del método
                                        puedan utilizar tantos parámetros como deseen sin afectar la compatibilidad de la abstracción.
        - **kwargs                  : "Argumentos con Nombres Variables", necesario para que las instancias del método
                                        puedan utilizar tantos argumentos con nombre (nombre = "Cielo", valor = 1)como desee sin afectar la compatibilidad de la abstracción.
    
    - Nota:
        - La utilización del parámetro *args permite utilizar diversos parámetros sin valor por defecto o nombre.
            En caso de haber múltiples parámetros, Python los tomará como una tupla.
        
        - La utilización del parámetro **kwargs  permite utilizar diversos parámetros con nombre o valor por defecto.
            En caso de haber múltiples parámetros con nombre, Python los tomará como un diccionario.
    """