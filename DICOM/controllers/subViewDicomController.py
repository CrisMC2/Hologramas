#=============================================
#Importamos Librerías
import sys
import os

#=============================================
#Extendemos el path del proyecto
_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

import numpy as np

#=============================================
#Importamos partes de librerías
from typing import Union

from PyQt5.QtWidgets import QApplication, QMainWindow #No eliminar QApplication, se utiliza en los test
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap

#=============================================
#Importamos clases/Métodos/Elementos del mismo proyecto
from views.subViewDICOM import Ui_subViewDicom     #Importamos la interfaz principal
from config import constantSubViewDICOM as consVDcm #Importamos las constantes
from core.classes.DicomMatrix import DicomMatrix
from services.DicomExtract import DicomExtract
from services.InformationDicom import InformationPatient, InformationStudySerie, InformationImage
from utils.Pixmap import Pixmap

class Ui_subViewDicomController(Ui_subViewDicom):
    """
    La clase Ui_subViewDicomController es la encargada de controlar
    la clase Ui_subViewDicom.
    
    - Ello implica controlar los valores que tendrán los elementos de la interfaz
        a lo largo de la ejecución de la misma
    
    """
    def __init__(self, widget_main: QWidget, 
                    layout_main: Union[QHBoxLayout, QVBoxLayout]):        
        super().__init__()

        #Instanciamos la vista subViewDicom y la ejecutamos mediante setupUi
        self.ui = Ui_subViewDicom()
        self.ui.setupUi(self.define_widget_main(widget_main, layout_main))
        
        self.create_objects() #Creamos las instancias de las clases necesarias para el controlador
    
    def define_widget_main(self, widget: QWidget, 
                            layout: Union[QHBoxLayout. QVBoxLayout]) -> tuple[QWidget, QHBoxLayout]:
        if isinstance(widget, QWidget) and isinstance(layout, [QHBoxLayout, QVBoxLayout]): 
            widget_main = widget
            layout_main = layout 
        else:
            raise ValueError("Los tipos de elemento proporcionados no corresponden a un QWidget y QLayout (QHBoxLayout, QVBoxLayout)")
        
        return widget_main, layout_main
    """
    El mètodo define_widget_main de la clase subViewDicomController.py 
    tiene la finalidad de verificar que si un widget y un layout 
    sean efectivamente elemento QWidget o QLayout

    - Paràmetros:
        - self (subViewDicomController)     : Instancia de la clase subViewDicomController.
        - widget (QWidget)                  : Widget sobre el cual se realizarà la verificaciòn.
        - layout (QHBoxLayout | QVBoxLayout): Layout sobre el cual se realizará la verificación.
    
    - Retorno:
        - tuple[QWidget, QLayout]   : Se retorna una tupla que contiene el elemento 
                                        QWidget y el elemento QLayout 

    - Exception:
        - ValueError        : En caso de que los parámetros widget y layout no tengan su 
                                valor correspondiente.
    """
    
    def change_static_info(self):
        if self.dicoms_utilities:
            self.define_values_items_static(self.dict_info_patient["PatientName"], self.dict_info_patient["PatientID"], 
                                            self.dict_info_patient["PatientBirthDate"], self.dict_info_patient["PatientSex"], 
                                            self.dict_info_study["InstitutionName"], self.dict_info_study["StudyInstanceID"],
                                            self.dict_info_study["BodyPartExamined"], self.dict_info_study["StudyDate"], 
                                            self.dict_info_study["StudyTime"])
    
    """
    Disparador => Cambiar el path de los dicom
    """
    
    def change_semi_dinamic_info(self, end_value_dicom_view: int):
        if self.dicoms_utilities:
            self.define_values_items_semi_dinamic(text_img_end=end_value_dicom_view,
                                                  value_end_slider=end_value_dicom_view)
    
    """
    Disparador => Cambiar la vista del folder dicom (Axial, Coronal y Sagital)
    """
    
    def change_dinamic_info(self, num_img_now: int, img: QPixmap):
        if self.dicoms_utilities:
            self.define_values_items_dinamic(num_img_now)
            self.define_value_image(img)
    
    """
    Disparador => Cambiar el valor del slider
    """


    def define_values_items_static(self, text_name: str, text_ID_patient: str, 
                                   text_date_born: str,  text_sex: str, 
                                   text_institution_name: str, text_study_ID: str,
                                   text_body_part: str, text_acquisition_test: str,
                                   text_acquisition_time: str,
                                   text_img: str = "IMG", 
                                   value_slider_now: int = consVDcm.DEFAULT_VALUE_SLIDER) -> None:
        self.ui_text_name.change_data(text_name)
        self.ui_text_ID_Patient.change_data(text_ID_patient)
        self.ui_text_date_born.change_data(text_date_born)
        self.ui_text_sex.change_data(text_sex)
        self.ui_text_institution_name.change_data(text_institution_name)
        self.ui_text_study_ID.change_data(text_study_ID)
        self.ui_text_body_part.change_data(text_body_part)
        self.ui_text_acquisition_test.change_data(text_acquisition_test)
        self.ui_text_acquisition_time.change_data(text_acquisition_time)
        self.ui_text_img.change_data(text_img)
        
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
    
    def define_values_items_semi_dinamic(self, text_img_end: str, 
                                         value_end_slider: int, value_start_slider: int = consVDcm.DEFAULT_VALUE_SLIDER) -> None:
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
    
    def define_values_items_dinamic(self, text_img_now: str,
                                        img: QPixmap) -> None:
        self.ui_text_img_now.change_data(text_img_now)
        self.ui_img_dicom.insert_element(img)
    """
    El método "define_values_items_semi_dinamic" cumple la función de darle valor
    a algunos elementos que conforman la vista DICOM
    
    - Estos elementos tienen la particularidad de que variarán constantemente a lo largo
        de la visualización de los archivos.
    - Ello pasa a razón de que esto variará según el QSlider
        
    - Parámetros:
        - text_img_now (str)        : Valor String que será usado para cambiar la data del elemento ui_text_img_now
        - img (QPixmap)         : Instancia de la clase QPixmap que contiene la imagen dicom
    """