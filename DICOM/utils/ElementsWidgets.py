from typing import Union, Callable
from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit, QSlider, QSizePolicy, QGraphicsProxyWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont

from abstracts.Ui.AbsSliderControl import AbsSliderControl
from abstracts.Ui.AbsTextControl   import AbsTextControl

class TextWidget(AbsTextControl):
    """
    El constructor nos permite generar una variable de clase (self)
    la cual se crea a partir de la instancia del parámetro pedido.
    
    - Parámetro:
        - type_element (QWidget)    : Elemento de text (Label, TextEdit, etc.) con el cual la clase
                                        trabajará.
    
    - Nota =>
        El parámetro necesita de una instancia de la clase QLabel, QTextEdit o similares; mas no
        de la clase como tal. 
        
    - Ejemplo:
        - Bien: TextWidget(QLabel())
        - Mal : TextWidget(QLabel) 
        
    """
    def __init__(self, type_element: Union[QLabel, QTextEdit]):
        if isinstance (type_element, (QLabel, QTextEdit)):
            self.q_text = type_element
                
        else:
            raise TypeError("El tipo de elementos que intentas incluir no es un Widget de texto: QLabel, QTextEdit")
    
    def configure_features(self, size_x: int, size_y: int,
                           minimum_size_x: int, minimum_size_y: int,  
                           size_policy_x: QSizePolicy, size_policy_y: QSizePolicy) -> None:
        
        self.q_text.setFixedSize(size_x, size_y)
        self.q_text.setMinimumSize(minimum_size_x, minimum_size_y)
        self.q_text.setSizePolicy(size_policy_x, size_policy_y)       

    def configure_behaivor(self, focus_policy: Qt):
        self.q_text.setFocusPolicy(focus_policy)
    
    
    def get_data(self):
        return self.q_text.getText()
    """
    El método get_data heredado en la clase TextWidget desde la clase padre AbsTextControl
    permite retornar el valor del elemento de texto inicializado en la clase.
    
    - Parámetros:
        - self (TextWidget)     : Instancia de la clase TextWidget
    
    - Retorno:
        - q_text.getText()      : Información (texto) que posee el elemento de texto 
                                    de la clase.
    
    """
    def change_data(self, new_data: str):
        self.q_text.setText(new_data)
    """
    El método change_data heredado en la clase TextWidget
    permite cambiar la data o el texto que tiene actualmente el elemento.
    
    - Parámetros:
        - self (TextWidget)     : Instancia de la clase TextWidget
        - new_data (str)        : Valor "string" usado para cambiar la data u información del elemento de texto.
    """
        
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

    def show_slider(self, show: bool):
        if show:
            self.q_slider.show()
        else:
            self.q_slider.hide()
    
    def define_range(self, start: int, end: int):
            if start and end: #Si tenemos ambos valores
                self.q_slider.setRange(start, end)
            elif start: #Si solo tenemos start
                self.q_slider.setMinimum(start)
            elif end: #Si solo tenemos end
                self.q_slider.setMaximum(start)    
    """
    El método "define_range" está pensado para cambiar los valores que tiene el Slider.
    
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
    
    def set_value(self, new_value: int):
        self.q_slider.setValue(new_value)
    
    """
    El método "set_value" heredado en SliderWidget está pensado para poder cambiar el 
    valor actual del slider.
    
    - Parámetros:
        - self (SliderWidget)   : Instancia de la clase SliderWidget
        - new_value (int)       : Valor "int" usado para cambiar el valor del slider.
    """
    def get_value(self) -> int:
        return self.q_slider.value()
    """
    El método "get_value" nos permite retornar el valor actual en el cual se encuentra el slider.
    
    - Retorno:
        - slider.value() => Retorna el valor actual en el cual se encuentra el Slider
    """
    
    def get_value_edit(self, difference: int) -> int:
        return self.q_slider.value()+difference

    """
    El método "get_value_edit" permite devolver el valor actual que tiene el slider
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
    
    def connect_change_value(self, function_connect: Callable[[int], None]) -> int:
        self.q_slider.valueChanged.connect(function_connect)