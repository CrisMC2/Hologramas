# Definir los valores de ajuste para los gestos
GESTO_DISPLACE_LEFT = -10
GESTO_DISPLACE_RIGHT = 10
GESTO_SCROLL_UP = -10
GESTO_SCROLL_DOWN = 10
GESTO_ZOOM_IN = 0.8
GESTO_ZOOM_OUT = 1.2

#CONCEPTOS USADOS EN LA INTERACCION DE GESTOS Y EL STL
"""
reader: Un objeto vtkSTLReader que se encarga de leer el archivo STL (el modelo 3D) para poder usarlo en el renderizado.

mapper: Un objeto vtkPolyDataMapper que toma los datos del modelo 3D proporcionados por el reader y los convierte en una forma que VTK puede renderizar y mostrar en la pantalla.

actor: El actor es un objeto en VTK que "posee" el modelo 3D, al que se le ha asignado un mapper. Es el objeto que se añade al renderizador para ser visualizado.

renderWindow: Es la ventana donde todo el contenido visual (el modelo 3D, la cámara, la textura, etc.) se va a mostrar.

renderer_cam: Un renderizador que se utiliza para visualizar el plano (con la textura) y la cámara. Se configura con un área de vista (viewport) y un fondo.

planeSource: Define un plano que se utilizará para aplicar una textura. El plano tiene tres puntos definidos: el origen y dos puntos más para definir su forma.

texture: La textura que se aplica al plano. Puede ser una imagen o datos visuales que cambian la apariencia del plano.

mapper_plane: Un vtkPolyDataMapper que convierte la geometría del plano en algo que puede ser visualizado.

actor_plane: Un actor que contiene el plano, al que se le ha asignado su mapper y su textura, y que se agrega al renderizador de la cámara.

renderer_stl: Otro renderizador, pero este se utiliza para visualizar el modelo STL en la parte principal de la ventana. Tiene un fondo blanco y ocupa el 70% de la ventana.
"""