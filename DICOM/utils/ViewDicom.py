import numpy as np

from core.classes.AbsDicomView import AbsDicomView

class ViewAxial(AbsDicomView):
    def define_aspect(self, label: str):
        pass
    
    """
    La implementación de create_view en ViewAxial
    utiliza la matriz de la vista creada mostrando solo una capa del espectro 3D a la vez.
    
    - La matriz es una serie de imágenes envueltas en un espectro 3D.
    - Ello significa, que si solo tomamos una capa, estaremos viendo solo una imagen.    

    Ejem:
    
    Img = 
    [ [[1, 2, 3, 4, 5]
       [6, 7, 8, 9, 10]]
      
      [[11, 12, 13, 14, 15]
       [16, 17, 18, 19, 20]]
    ]
    
    Si elegimos Img[0, :, :] nos devolverá:
    
    [[1, 2, 3, 4, 5]
       [6, 7, 8, 9, 10]]
       
    Esto representaría una imagen, pero solo con un canal (Escala de grises)
    
    Y si elegimos: Img[1, :, :], tendríamos otra imagen, pero con los elementos de la fila y columna diferentes,
    lo mismo pasa con el archivo dicom, al solo usar la matriz, simulamos tener una imagen.
    
    
    """
    def create_view(self, array_dicoms: np.array, i: int):
        return array_dicoms[i,:,:]
    
class ViewSagittal(AbsDicomView):
    def define_aspect(self, label: str):
        pass
    
    """
    En el caso de ViewSagittal, que es la vista desde la perspectiva de "perfil",
    debemos hacer que la matriz solo muestre una vista de perfil.
    
    Ello es posible si hacemos que todas las capaz y todas las columnas de una misma fila se muestren a la vez.
    
    
    Ejemplo:
    Esto es más fácil de notar con 2 hojas de papel.
    
    - Pon ambas hojas en posición vertical, una mirando hacia ti de frente y otra de perfil.
    - Luego, coloca la hoja en posición de "perfil" en uno de los extremos de la hoja frente a ti.
    - A continuación, pasa horizontalmente la hoja en posición de perfil a través de toda la hoja que está frente a ti sin cambiar de la 
            "posición de perfil" hasta llegar al otro extremo.
    
    Este sencillo ejercicio te muestra como es que la tomografía muestra la vista Sagittal. 
    La hoja que está frente a ti sería la persona, y la de perfil sería como la cámara. Es como si estuvieras entrando a una persona desde un lateral hasta otro.
    
    """
    def create_view(self, array_dicoms: np.array, i: int):
        return array_dicoms[:,:,i]

class ViewCoronal(AbsDicomView):
    def define_aspect(self, label: str):
        pass
    
    """
    En el caso de ViewCoronal, que es la vista desde la perspectiva de "frente",
    debemos hacer que la matriz solo muestre una vista de frente.
    
    Ello es posible si hacemos que todas las capaz y todas las filas de una misma columna se muestren a la vez.
    
    
    Ejemplo:
    Esto es más fácil de notar con una caja y una hoja de papel.
    
    - La hoja de papel debe adentrarse en la caja verticalmente, como si estuviera "de pie".
    - Luego, coloca la hoja de papel (verticalmente) en uno de los extremos de la caja (sin salir de la misma).
    - A continuación, solo desplaza la hoja (aún verticalmente) hasta el otro extremo de la caja.
    
    Si repites el mismo proceso, pero mirando a la caja desde el mismo sentido desde el que avanza la hoja, verás como esta pasa por todo de una forma "frontal".
    Ahora imagina que la caja es el cuerpo humano, y la hoja el proceso de la tomografía.
    """
    def create_view(self, array_dicoms: np.array, i: int):
        return array_dicoms[:,i,:]