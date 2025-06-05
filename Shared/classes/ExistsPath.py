import os

class ExistsPath():
    def exists(self, path: str, create: bool=False):
        if path:
            if os.path.exists(path):
                return True
            
            elif create:
                os.makedirs(path)
                return True
            
            else:
                return False
        
        else:
            raise ValueError("ExistsPath-> exists: El path indicado no existe")
    """
    El siguiente método verifica si una dirección existe
    
    - Además, permite crear una dirección en caso de que no exista (Por medio de un parámetro booleano)
    
    Parámetros:
        - self (Instancia de clase)     : Instancia de la clase AbsDicomPaths_
        - path (str)                    : Dirección de la cual se verifica la existencia
        - create (bool)                 : Confirmar si se desea crear o no la dirección.
        
    Retorno:
        - bool          : 'True' si la dirección existe o es creada
                          'False' si la dirección no existe y se espicifica que no debe ser creada
    """
        