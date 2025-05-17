from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFrame
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt, QRectF


#=================================================================================================
#Configuración del Controlador
DEFAULT_CANT_VIEWS_DICOM = 1
DEFAULT_VIEW_DICOM = "Axial View"
DEFAULT_NUM_DICOM = 1
DEFAULT_DIFFERENCE_VALUE_SLIDER = 1 
"""
Este apartado hace alución a cuánto le agregaremos 
o quitaremos al valor final del slider. 

- Ejm: 
	o "1" => El valor del slider será aumentado en 1
	o "-1" => El valor del slider será disminuido en 1
"""

VIEW_DICOM_INCONSTANT = DEFAULT_VIEW_DICOM
"""
VIEW_DICOM_INCONSTANT será la variable que guarde la vista que irá teniendo la interfaz a lo largo
de la ejecución del programa.
"""



#=================================================================================================
#Configuración Características de GraphicsView
# SCROLL_BAR_POLICY_DEFAULT = Qt.ScrollBarAsNeeded
SCROLL_BAR_POLICY_DEFAULT = Qt.ScrollBarAlwaysOn


FRAME_STYLE_DEFAULT = QFrame.NoFrame

"""
setFrameStyle(QFrame.NoFrame): Elimina el borde del QGraphicsView

"""

DEFAULT_CENTER_ON = True
DEFAULT_FIT_IN_VIEW = False

#=================================================================================================
#Configuración Comportamiento de GraphicsView

DEFAULT_VIEW_SIZE_POLICY = QSizePolicy.Preferred

DRAG_MODE_DEFAULT     = QGraphicsView.ScrollHandDrag
"""
- setDragMode(QGraphicsView.NoDrag): Desactiva el arrastre de la escena.
- setDragMode(QGraphicsView.ScrollHandDrag): Permite arrastrar la escena como si fuera un "scroll".
- setDragMode(QGraphicsView.RubberBandDrag): Permite seleccionar múltiples elementos con una caja de selección.

"""

INTERACTIVE_DEFAULT   = True
"""
- setInteractive(True) : Activa la interactividad con los elementos gráficos.
                (False): Deshabilitar la interactividad
"""

RESIZE_ANCHOR_DEFAULT = QGraphicsView.AnchorUnderMouse
"""
setResizeAnchor(QGraphicsView.AnchorUnderMouse): Mantiene el cursor como punto de referencia al redimensionar.
"""

VIEW_PORT_UPDATE_MODE_DEFAULT = QGraphicsView.BoundingRectViewportUpdate
"""
setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate): Optimiza la actualización de la vista.
"""





#=================================================================================================
#Configuración Características de GraphicScene
SCENE_RECT_DEFAULT = QRectF(0, 0, 600,800)
ITEM_INDEX_METHOD_DEFAULT = QGraphicsScene.NoIndex



#=================================================================================================
#Configuración del QGraphicsWidget
DEFAULT_WIDGET_MINIMUM_SIZE_X = 900
DEFAULT_WIDGET_MINIMUM_SIZE_Y = 450

DEFAULT_G_VIEW_SIZE_POLICY = QSizePolicy.Fixed

#Configuración del Layout a usar en QGraphicsWidget
#Configuración del Layout Principal (Main) (GridLayout)
DEFAULT_ROWS_LAYOUT = 10
"""
La configuración DEFAULT_ROWS_LAYOUT permite configurar la cantidad de rows (filas)
que tendrá el GridLayout.
"""

DEFAULT_COLS_LAYOUT = 4
"""
La configuración DEFAULT_COLS_LAYOUT permite configurar la cantidad de cols (columnas)
que tendrá el GridLayout.
"""

LIST_DICT_ROWS_STRETCH = [{"row": 1, "stretch": 0}, {"row": 2, "stretch": 0},
                             {"row": 3, "stretch": 0}, {"row": 4, "stretch": 0},
                             {"row": 5, "stretch": 0}, {"row": 6, "stretch": 0},
                             {"row": 7, "stretch": 2}, {"row": 8, "stretch": 0},#5
                             {"row": 9, "stretch": 0}, {"row": 10, "stretch": 0}] #Lista de diccionarios.

LIST_DICT_COLS_STRETCH = [{"col": 1, "stretch": 1}, {"col": 2, "stretch": 0}, #7
                              {"col": 3, "stretch": 2}, {"col": 4, "stretch":0}]

DEFAULT_SPACING_MAIN = 0

#=================================================================================================
#Configuración de los Elementos del lado derecho
DEFAULT_ALIGNMENT_RIGHT = Qt.AlignRight

#=================================================================================================
#Configuración de los Elementos del lado izquierdo
DEFAULT_ALIGNMENT_LEFT = Qt.AlignLeft

#Configuración del Layout Izquierdo (LayoutItem)
DEFAULT_ORIENTATION_LAYOUT_1 = "H" 
"""
La configuración DEFAULT_ORIENTATION_LAYOUT_1 define si el Layout será vertical y horizontal.

    - H     : Horizontal
    - V     : Vertical
"""

#Configuración del Layout Central (LinearLayout)
DEFAULT_ORIENTATION_LAYOUT_2 = "V" 
"""
La configuración DEFAULT_ORIENTATION_LAYOUT_2 define si el Layout será vertical y horizontal.

    - H     : Horizontal
    - V     : Vertical
"""

#=================================================================================================
#Configuración los widget a usar con los Layout / GridLayout y demás

DEFAULT_LEFT_MARGIN   = 0
DEFAULT_RIGHT_MARGIN  = 0
DEFAULT_TOP_MARGIN    = 0
DEFAULT_BOTTOM_MARGIN = 0

DEFAULT_SPACING = 0

DEFAULT_LAYOUT_SIZE_POLICY_X = QSizePolicy.Preferred
DEFAULT_LAYOUT_SIZE_POLICY_Y = QSizePolicy.Fixed

#=================================================================================================
#Configuración del QGraphicsProxyWidget
DEFAULT_PROXY_SIZE_POLICY_X = QSizePolicy.Preferred
DEFAULT_PROXY_SIZE_POLICY_Y = QSizePolicy.Preferred


#=================================================================================================
#Configuración del slider
DEFAULT_TYPE_SLIDER = "V"
"""
La configuración DEFAULT_TYPE_SLIDER define si el Slider será vertical y horizontal.

    - H     : Horizontal
    - V     : Vertical
"""

DEFAULT_VALUE_SLIDER = 1
"""
La configuración DEFAULT_VALUE_SLIDER define el valor que tendrá o en el que se 
encontrará el slider.

"""

#=================================================================================================
#Configuración de los QLabel
DEFAULT_TEXT_MINIMUM_SIZE_X = 10
DEFAULT_TEXT_MINIMUM_SIZE_Y = 10
DEFAULT_TEXT_SIZE_POLICY_X = QSizePolicy.Expanding
DEFAULT_TEXT_SIZE_POLICY_Y = QSizePolicy.Preferred
DEFAULT_WRAP_MODE = True



#=================================================================================================
#Configuración del QLabel del QPixmap
DEFAULT_PIXMAP_SIZE_POLICY_X = QSizePolicy.Fixed
DEFAULT_PIXMAP_SIZE_POLICY_Y = QSizePolicy.Fixed


#=================================================================================================
#Configuración de los spacers horizontales
DEFAULT_SPACER_H_SIZE_POLICY_X = QSizePolicy.Expanding
DEFAULT_SPACER_H_SIZE_POLICY_Y = QSizePolicy.Preferred

#=================================================================================================
#Configuración de los spacers verticales
DEFAULT_SPACER_V_SIZE_POLICY_X = QSizePolicy.Expanding
DEFAULT_SPACER_V_SIZE_POLICY_Y = QSizePolicy.Expanding