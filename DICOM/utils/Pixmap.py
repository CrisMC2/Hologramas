import numpy as np

from PyQt5.QtGui import QImage, QPixmap
from abstracts.Ui.AbsPixmap import AbsProccessPixmap

class Pixmap(AbsProccessPixmap):
    
    def create_pixmap(self, img_array: np.uint8) -> QPixmap:
        self.prepare_array(img_array)
        
        #QImage (data, width, height, bytesPerLine, format)
        qimg = QImage(img_array, img_array.shape[0], img_array.shape[1], img_array.strides[0], QImage.Format_Grayscale8)
        img_pix_map = QPixmap.fromImage(qimg)
        
        return img_pix_map
    """
    El método create_pixmap tiene por objetivo el convertir un array 2D en un elemento Pixmap
    compatible con elementos como QGraphicsScene.
    
    - Primero verificamos que el arreglo sea correcto para ser utilizado en un QImage 
    - Se crea un elemento QImage, capaz de interpretar los datos directamente desde el array que proporcionaremos.
    - Luego se crea un elemento QPixmap a partir del elemento QImage creado anteriormente.
    
    - Parámetros
        - self (Pixmap)         : Instancia de la clase Pixmap.
        - img_array(np.uint8)   : Array que contiene la información de la imagen en formato "uint8".
    
    - Retorno
        - img_pix_map (QPixmap) : Elemento QPixmap procesado a partir del arreglo inicial
        
    Nota: QPixmap no permite leer datos directamente desde, por ejemplo, un array; es por esta razón que 
            se usa de intermediario al elemento QImage, ya que, QPixmap sí permite interpretar 
            datos directamente desde un QImage. 
    """
    
    def prepare_array(self, img_array: np.array) -> np.uint8:
        if img_array.dtype != np.uint8:
            img_array = img_array.astype(np.uint8)
        
        if not img_array.flags["C_CONTIGUOUS"]:
            img_array = np.ascontiguousarray(img_array)
        
        return img_array
    """
    El método provee la opción de preparar un array para una futura utilización 
    en elementos como QImage o semejantes.
    
    - Hacemos que el formato de los datos del arreglo sea np.uint8
    - Nos aseguramos de que el formato del arreglo sea "row major-orden" 
        (significa que las filas se guardarán de manera continua en la memoria),
        esta forma es la configuración por defecto que da numpy, y es la que utiliza la biblioteca "Q".
    
    - Parámetros:
        - self (Pixmap)         : Instancia de la clase Pixmap.
        - img_array(np.uint8)   : Array que contiene la información de la imagen en formato "uint8".
    
    - Retorno
        - img_pix_map (np.uint8) : Array ya procesado.
    """ 