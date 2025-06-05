#60 FRAMES
import cv2
import numpy as np
import vtk

# Importar las configuraciones de los gestos desde un archivo externo
from PyQt5.QtCore import pyqtSignal
from Modeling_3D.config import constantGestureMove as consGesMo
from vtkmodules.vtkCommonCore import vtkOutputWindow
from Gestures.main_ import EmitGest

# # Clase personalizada para manejar los mensajes de salida de VTK (evitar errores en consola)
class MyVTKOutputWindow(vtkOutputWindow):
    def DisplayText(self, text: str) -> None:
        pass  
    
vtkOutputWindow.SetInstance(MyVTKOutputWindow())


# Clase principal para manejar la interacción de gestos con el modelo 3D
class GestureInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, renderer_stl, actor: vtk.vtkActor, renderer_cam, texture) -> None:
        super().__init__()
        self.renderer_stl = renderer_stl  # Renderizador del modelo STL
        self.actor = actor
        self.renderer_cam = renderer_cam  # Renderizador de la cámara
        self.texture = texture
    
    def connect_execute(self, signal: pyqtSignal):
        signal.connect(self.on_signal)
    
    """
    La función "connect_execute" de la clase "GestureInteractorStyle" tiene como objetivo
    conectar una señal al método que da comienzo a la interacción con el render_stl.
    
    - Parámetros:
        - signal (pyqtSignal[object, object]):      Señal que emite 2 elementos de tipo object.
    """
        
        
    def on_signal(self, frame: cv2.typing.MatLike, gesture: str) -> None:
        self.apply_gesture(gesture)  # Aplicar la transformación correspondiente al modelo 3D
        # self.update_camera_texture(frame)
        # self.renderer_cam.GetRenderWindow().Render()
        self.renderer_stl.GetRenderWindow().Render()
        
    
    """
    Método que se ejecuta cada vez que el temporizador se activa. Captura el fotograma de la cámara,
    procesa el gesto y lo aplica al modelo 3D.
    """
        
    def update_camera_texture(self, frame: np.ndarray) -> None:
        """
        Actualiza la textura de la cámara en el renderizador VTK con el fotograma procesado.
        """
        h, w, _ = frame.shape
        vtk_image = vtk.vtkImageImport()  # Crear una imagen VTK a partir del fotograma
        vtk_image.CopyImportVoidPointer(frame.tobytes(), len(frame.tobytes()))  # Convertir el fotograma en bytes
        vtk_image.SetDataScalarTypeToUnsignedChar()
        vtk_image.SetNumberOfScalarComponents(3)
        vtk_image.SetDataExtent(0, w-1, 0, h-1, 0, 0)
        vtk_image.SetWholeExtent(0, w-1, 0, h-1, 0, 0)
        vtk_image.Update()  # Actualizar la imagen

        self.texture.SetInputConnection(vtk_image.GetOutputPort())


    def apply_gesture(self, gesture: str) -> None:
        """
        Aplica la transformación correspondiente al gesto detectado en la cámara 3D.
        """
        cam = self.renderer_stl.GetActiveCamera()
        if gesture == "Displace_Left":
            cam.Azimuth(consGesMo.GESTO_DISPLACE_LEFT)
        elif gesture == "Displace_Right":
            cam.Azimuth(consGesMo.GESTO_DISPLACE_RIGHT)
        elif gesture == "Scroll_Up":
            cam.Elevation(consGesMo.GESTO_SCROLL_UP)
        elif gesture == "Scroll_Down":
            cam.Elevation(consGesMo.GESTO_SCROLL_DOWN)
        elif gesture == "Zoom_In":
            cam.Dolly(consGesMo.GESTO_ZOOM_IN)
            self.renderer_stl.ResetCameraClippingRange()
        elif gesture == "Zoom_Out":
            cam.Dolly(consGesMo.GESTO_ZOOM_OUT)
            self.renderer_stl.ResetCameraClippingRange()

        # self.renderer_stl.GetRenderWindow().Render()