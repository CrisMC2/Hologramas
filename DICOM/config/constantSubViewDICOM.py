from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFrame
from PyQt5.QtGui import QColor


#=================================================================================================
#Configuración Características de GraphicsView
"""
Para poder utilizar un setBackgroundBrush necesitamos un valor Brush
Y este puede utilizar un QColor, el cual permite utilizar colores en formato RGB
"""
BACKGROUND_COLOR_DEFAULT = QColor(255,0,0)#QColor(70, 70, 70)

"""
setFrameStyle(QFrame.NoFrame): Elimina el borde del QGraphicsView

"""
FRAME_STYLE_DEFAULT = QFrame.NoFrame


#=================================================================================================
#Configuración Comportamiento de GraphicsView
"""
- setDragMode(QGraphicsView.NoDrag): Desactiva el arrastre de la escena.
- setDragMode(QGraphicsView.ScrollHandDrag): Permite arrastrar la escena como si fuera un "scroll".
- setDragMode(QGraphicsView.RubberBandDrag): Permite seleccionar múltiples elementos con una caja de selección.

"""
DRAG_MODE_DEFAULT     = QGraphicsView.ScrollHandDrag

"""
- setInteractive(True) : Activa la interactividad con los elementos gráficos.
                (False): Deshabilitar la interactividad
"""
INTERACTIVE_DEFAULT   = True

"""
setResizeAnchor(QGraphicsView.AnchorUnderMouse): Mantiene el cursor como punto de referencia al redimensionar.
"""
RESIZE_ANCHOR_DEFAULT = QGraphicsView.AnchorUnderMouse

"""
setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate): Optimiza la actualización de la vista.

"""
VIEW_PORT_UPDATE_MODE_DEFAULT = QGraphicsView.BoundingRectViewportUpdate





#=================================================================================================
#Configuración Características de GraphicScene
QGraphicsScene.NoIndex


