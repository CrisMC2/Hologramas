from typing import List, Dict, Union

from PyQt5.QtWidgets import QGraphicsLinearLayout, QGraphicsLayoutItem, QGraphicsGridLayout, QGraphicsWidget, QGraphicsProxyWidget, QGraphicsPixmapItem, QSizePolicy
from PyQt5.QtCore import Qt

from abstracts.Ui.AbsLayout import AbsLayout

class LinearLayout(AbsLayout):
    """
    La clase "GraphicsLayout" está especializada en la creación de Layouts para la interacción con 
    las clases "Graphics", como QGraphicsScene, QGraphicsWidget o inclusive otros Layout como "QGraphicsGridLayout".
    
    En este clase se consideran Layouts como QGraphicsLinearLayout o QGraphicsLayoutItem.
    
    """
    def __init__(self, type_layout: Union[type[QGraphicsLinearLayout], type[QGraphicsLayoutItem]],
                 orientation_layout: str):
        self.create_layout(type_layout, orientation_layout)
    
    def create_layout(self, type_layout: Union[type[QGraphicsLinearLayout], type[QGraphicsLayoutItem]], 
                      orientation_layout: str):
        if orientation_layout == "V":
            self.q_layout = type_layout(Qt.Vertical)
            
        elif orientation_layout == "H":
            self.q_layout = type_layout(Qt.Horizontal)
        
        else:
            raise ValueError("El parámetro type_layout ingresado no es correcto. Intenta con: V | H")
    """
    El método create_layout nos sirve para crear el Layout que cumplirá el labor del 
    GraphicsWidget. 
    
    - La creación del mismo varía de acorde al parámetro type_layout.
    
    - Parámetros:
        - type_layout (Union[type[QGraphicsLinearLayout], type[QGraphicsLayoutItem]])   : Determina la instancia que utilizará el layout,
                                                                                            siendo la clase QGraphicsLinearLayout o la clase QGraphicsLayoutItem
        - orientation_layout (str)       : Define si el Layout será vertical u horizontal
    
    """ 
    def configure_features(self, left_margin: float, right_margin: float, 
                            top_margin: float, bottom_margin: float, spacing: float):
        self.q_layout.setContentsMargins(left_margin, right_margin, top_margin, bottom_margin)
        self.q_layout.setSpacing(spacing)
        # self.q_layout.setAlignment(Qt.AlignRight)
    
    def configure_behavior(self, size_policy_x: QSizePolicy, size_policy_y: QSizePolicy):
        self.q_layout.setSizePolicy(size_policy_x, size_policy_y)
        
    
    def insert_element(self, list_elements: list[Union[QGraphicsWidget, QGraphicsProxyWidget, QGraphicsPixmapItem]]):
        for ele in list_elements:
            if isinstance(ele, (QGraphicsWidget, QGraphicsProxyWidget, QGraphicsPixmapItem)):
                self.q_layout.addItem(ele)
                
            else:
                raise ValueError(f"El elemento: {ele} no pudo ser agregado al Layout al no ser un elemento derivado de QWidget")
        
        
        

class GridLayout(AbsLayout):
    def __init__(self, num_rows: int, num_cols: int):
        self.create_layout(num_rows, num_cols)
    
    def create_layout(self, num_rows: int, num_cols: int):
        if num_rows and num_cols:
            self.q_grid_layout = QGraphicsGridLayout()
            
            self.num_rows = num_rows
            self.num_cols = num_cols
    
    def configure_features(self, rows_stretch: List[Dict[int, int]], 
                                 columns_stretch: List[Dict[int, float]], spacing: float, 
                                 margin_left: int, margin_top: int, margin_right: int, margin_bottom: int):
        if len(rows_stretch) != self.num_rows or len(columns_stretch) != self.num_cols:
            raise ValueError("La cantidad de filas y columnas indicadas en los diccionarios no es igual a la cantidad existente.")
        
        else:
            #Configuramos el valor de las filas (rows)
            for rows in rows_stretch: #Primero iteramos respecto a la lista
                # for row, stretch in rows.keys(): #Y luego respecto a los items / elementos
                row, stretch = rows.keys() #Usamos la función keys para identificar los nombres de las keys del diccionario
                self.q_grid_layout.setRowStretchFactor(rows[row], rows[stretch])
            
            #Configuramos el valor de las columnas (col)
            for columns in (columns_stretch):
                col, stretch = columns.keys()
                self.q_grid_layout.setColumnStretchFactor(columns[col], columns[stretch])
            
            self.q_grid_layout.setSpacing(spacing)   
            self.q_grid_layout.setVerticalSpacing(spacing)            
        
        # self.q_grid_layout.setContentsMargins(margin_left, margin_top, margin_right, margin_bottom)
        self.q_grid_layout.setContentsMargins(margin_left, margin_top, margin_right, margin_bottom)
    
    """
    El método "configure_features" permite configurar las características base del GridLayout, 
    como el espaciado entre los elementos, el tamaño de cada fila y columna.
    
    - El método verifica si la cantidad de filas y columnas ingresadas es igual a la cantidad especificada inicialmente.
    
    - Parámetros:
        - self (GridLayout)     : Instancia de la clase GridLayout
        - rows_stretch (list[dict[int, float]])     : Lista de diccionarios usados para la configuraciónn del stretch 
                                                        de las filas / rows
        - columns_stretch (list[dict[int, float]])  : Lista de diccionarios usados para la configuración del stretch
                                                        de las columnas / columns
    
    - Notas:
    Los diccionarios están establecidos como parámetros con la intención de facilitar
    la inserción de datos.
    
    Como recomendación define a los diccionarios de la siguiente manera (Mira los keys, no los datos):
    
        dict_rows {
            row: 1,
            stretch: 0.1            
        }
        
        dict_cols {
            col: 1,
            stretch: 0.2
        }
    
    """
        
    def configure_behavior(self):
        pass
    
    def insert_element(self, elements_position: List[dict[QGraphicsProxyWidget, int, int, int, int]], alignment: Qt.Alignment):
        if elements_position:
            for element in elements_position:
                ele, row, col, row_span, col_span = element.keys() #Iteramos en lugar de usar los valores directamente desde el diccionario.
                self.q_grid_layout.addItem(element[ele], 
                                           element[row], element[col], 
                                           element[row_span], element[col_span], alignment=alignment)
        
    """
    El método insert_element instanciado en la clase GridLayout cumple la función de insertar una
    serie de elementos dentro de las posiciones existentes en el GridLayout.
    
    Ello implica que se verificará que no se ingrese una posición que no corresponda al layout.
    
    El método tiene una especie de orden en cuestión de sobreescribir la información; debido a que se considera
    el "span" de las filas y columnas (un elemento puede abarcar varias filas / columnas), hay que considerar que
    el elemento que se encuentre en la última posición puede sobreescribir a uno que esté en la primera posición
    en caso de que no se utilicen bien las posiciones.
    
    - Parámetros:
        - self (GridLayout)         : Instancia de la clase GridLayout
        - elements_position: list[dict[QWidget, int, int, int, int]]  :   Lista de elementos en forma de diccionario que se insertarán
                                                                            en las posiciones row, col, row_span, col_span especificadas.
                                                                
    - Nota:
    Para evitar problemas e inconvenientes con la ejecución del código, define a los diccionarios 
    de la siguiente manera (Mira los keys, no los datos):
    
        dict_element_position {
            element: QLabel,
            row: 1,
            col: 1,
            row_span: 1,
            col_span: 1
        }
        
    """