import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QSlider
from PyQt5.QtCore import Qt

from core.viewsUI.AbsSliderControl import AbsSliderControl
from core.viewsUI.AbsTextControl   import AbsTextControl

class TextWidget(AbsTextControl):
    """
    El constructor nos permite 
    """
    def __init__(self, type_element: QWidget):
        if isinstance (type_element, QLabel) or isinstance(type_element, QTextEdit):
            self.text = type_element
        
        else:
            print("El tipo de elementos que intentas incluir no es un Widget de texto.")
    
    def get_data(self):
        return self.text.getText()
    
    def change_data(self, new_data):
        self.text.setText(new_data)
        
class SliderWidget(AbsSliderControl):
    """
    Al heredar la clase no olvides agregar al constructor de la clase hija:
    
    - super().__init__(qslider_clase_hija)
    
    Esto hará que la clase padre pueda trabajar con la instancia que necesita.
    
    - Parámetros:
        - type_qslider      : Este parámetro permite decidir si el slider será vertical u horizontal.
        
    """
    def __init__(self, type_qslider: str):
        if type_qslider == 'V':
            self.q_slider = QSlider(Qt.Vertical)
        elif type_qslider == 'H':
            self.q_slider = QSlider(Qt.Horizontal)

    """
    El método está pensado para cambiar los valores que tiene el Slider.
    
    - Parámetros:
        - start (int)   => Define el valor inicial que tendrá el Slider.
        - end   (int)   => Define el valor final que tendrá el Slider.
    
    - Nota:
        - El método distingue si solo deseas cambiar el valor máximo,
          el valor mínimo o ambos.
        
    
    - Ejemplo:
        - Si solo se desea cambiar el valor inicial
            define_range(start = 10, end = None)
            
        - Si solo se desea cambiar el valor final:
            define_range(start = None, end = 100)
        
        - Si se desea cambiar ambos valores:
            define_range(start = 10, end = 100)
    """
    def define_range(self, start: int, end: int):
        if self.q_slider:
            if start and end: #Si tenemos ambos valores
                self.q_slider.setRange(start, end)
            elif start: #Si solo tenemos start
                self.q_slider.setMinimum(start)
            elif end: #Si solo tenemos end
                self.q_slider.setMaximum(start)
        else:
            print("El Slider aún no ha sido creado")
            
    def show_slider(self, show: bool):
        if show:
            self.q_slider.show()
        else:
            self.q_slider.hide()
    
    """
    El siguiente método nos permite retornar el valor actual en el cual se encuentra el slider.
    
    - Retorno:
        - slider.value() => Retorna el valor actual en el cual se encuentra el Slider
    """
    def get_value(self):
        return self.q_slider.value()
    
    """
    El siguiente método permite devolver el valor actual que tiene el slider
    dándole un pequeño cambio por medio de un parámetro:
    
    - Parámetros:
        - difference (int) : Es el valor en el que cambiará el valor del slider
    
    - Ejemplos:
        - Queremos que el valor del slider se retorne en 5 más.
            get_value_edit(5)
            valor del slider = 10
            
            Retorno => 10 + 5
             
        - Queremos que el valor del slider se retorne en 10 menos.
            get_value_edit(-10)
            valor del slider = 2
            
            Retorno => 2 - 10
    """
    def get_value_edit(self, difference: int):
        return self.q_slider.value()+difference