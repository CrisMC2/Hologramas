from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFrame
from PyQt5.QtGui import QColor


#=================================================================================================
#Configuración Características de GraphicsView

BACKGROUND_COLOR_DEFAULT = QColor(70, 70, 70)
"""
Para poder utilizar un setBackgroundBrush necesitamos un valor Brush
Y este puede utilizar un QColor, el cual permite utilizar colores en formato RGB
"""

FRAME_STYLE_DEFAULT = QFrame.NoFrame

"""
setFrameStyle(QFrame.NoFrame): Elimina el borde del QGraphicsView

"""

#=================================================================================================
#Configuración Comportamiento de GraphicsView

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
SCENE_RECT_DEFAULT = (0, 0, 600,800)

BACKGROUND_COLOR_DEFAULT_2 = QColor(0,0,0)

ITEM_INDEX_METHOD_DEFAULT = QGraphicsScene.NoIndex


#=================================================================================================
#Configuración del GraphicsWidget
DEFAULT_TYPE_LAYOUT = "H"
"""
La configuración DEFAULT_TYPE_LAYOUT define si el Layout será vertical y horizontal.

    - H     : Horizontal
    - V     : Vertical
"""


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