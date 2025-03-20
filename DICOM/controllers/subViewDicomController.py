import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from PyQt5.QtWidgets import QApplication, QMainWindow

from views.subViewDICOM import Ui_subViewDicom     #Importamos la interfaz principal
from config import constantSubViewDICOM as consVDcm #Importamos las constantes

class Ui_subViewDicomController(Ui_subViewDicom, QMainWindow):
    """
    La clase Ui_subViewDicomController es la encargada de controlar
    la clase Ui_subViewDicom.
    
    - Ello implica controlar los valores que tendrán los elementos de la interfaz
        a lo largo de la ejecución de la misma
    
    """
    def __init__(self):
        super().__init__()
        self.ui_subviewDicom = Ui_subViewDicom()
    
    
    def define_values_items_static(self, text_name: str, text_date_born: str,  text_date_test: str, 
                                   text_part_body: str, text_img: str = "IMG", 
                                   value_slider_now: int = consVDcm.DEFAULT_VALUE_SLIDER):
        self.ui_text_img.change_data(text_img)
        self.ui_text_name.change_data(text_name)
        self.ui_text_date_born.change_data(text_date_born)
        self.ui_text_date_test.change_data(text_date_test)
        self.ui_text_part_body.change_data(text_part_body)
        
        self.ui_slider.set_value(value_slider_now)
    
    """
    El método "define_values_items_static" cumplea la función de darle valor
    a los elementos que conforman la vista DICOM.
    
    - Estos valores tienen la particularidad de qué serán valores que no variarán a lo largo de 
        la visualización de los archivos DICOM.
    
    - Parámetros:
        - self (subViewDICOM)       : Instancia de la clase subViewDICOM
        - text_img (str)            : 
        - text_name (str)           :
        - text_date_born (str)      : 
        - text_part_body (str)      :
        - text_date_test (str)      :
        - value_slider_now (int)    :
        
    """
    
    def define_values_items_semi_dinamic(self, text_img_end: str, value_start_slider: int, value_end_slider: int):
        self.ui_text_img_end.change_data(text_img_end)
        self.ui_slider.define_range(value_start_slider, value_end_slider)
    
    """
    El método "define_values_items_semi_dinamic" cumple la función de darle valor
    a algunos elementos que conforman la vista DICOM
    
    - Estos elementos tienen la particularidad de que cambiarán a lo largo de la visualización, 
        pero en muy contadas ocasiones.
    
    - Parámetros:
        - value_start_slider (int)  : Valor Int encargado de definir el valor mínimo o inicial que tendrá el Slider
        - value_end_slider (int)    : Valor Int encargado de definir el valor máximo o final que tendrá el Slider
    """
    
    def define_values_items_dinamic(self, text_img_now: str):
        self.ui_text_img_now.change_data(text_img_now)
    
    """
    El método "define_values_items_semi_dinamic" cumple la función de darle valor
    a algunos elementos que conforman la vista DICOM
    
    - Estos elementos tienen la particularidad de que variarán constantemente a lo largo
        de la visualización de los archivos.
        
    - Parámetros:
        - text_img_now (str)        : Valor String que será usado para cambiar la data del elemento ui_text_img_now
    """