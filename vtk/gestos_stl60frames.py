#60 FRAMES

import sys
import os
import cv2
import numpy as np
import vtk
import tensorflow as tf
from typing import Optional

# Importar funciones reutilizables
from Reconocimiento_gestual.Prediction.main.Nuevo.ejecucion_conv_60 import configurar_rutas, inicializar_componentes

# Configurar paths para importar módulos personalizados
configurar_rutas()

# Cargar modelo, detector de manos y helper
modelo, landmark, help_predictor, labels = inicializar_componentes()

# Importar las configuraciones de los gestos desde un archivo externo
from gesture_settings import (
    GESTO_DISPLACE_LEFT,
    GESTO_DISPLACE_RIGHT,
    GESTO_SCROLL_UP,
    GESTO_SCROLL_DOWN,
    GESTO_ZOOM_IN,
    GESTO_ZOOM_OUT
)


from vtkmodules.vtkCommonCore import vtkOutputWindow
# # Clase personalizada para manejar los mensajes de salida de VTK (evitar errores en consola)
class MyVTKOutputWindow(vtkOutputWindow):
    def DisplayText(self, text: str) -> None:
        pass  
vtkOutputWindow.SetInstance(MyVTKOutputWindow())

# Clase principal para manejar la interacción de gestos con el modelo 3D
class GestureInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, renderer_stl, actor, renderer_cam, texture, cap) -> None:
        self.AddObserver("TimerEvent", self.on_timer)  # Establecer un observador para los eventos de temporizador
        self.renderer_stl = renderer_stl  # Renderizador del modelo STL
        self.actor = actor
        self.renderer_cam = renderer_cam  # Renderizador de la cámara
        self.texture = texture
        self.cap = cap
        self.gesture = None
        self.landmarks = []

    def on_timer(self, obj, event) -> None:
        """
        Método que se ejecuta cada vez que el temporizador se activa. Captura el fotograma de la cámara,
        procesa el gesto y lo aplica al modelo 3D.
        """
        ret, frame = self.cap.read()  # Captura un fotograma de la cámara
        if not ret:
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = landmark.drawHands(frame, True)
        self.landmarks = landmark.guardar_frames(frame, 60)

        if self.landmarks:
            array_landmark = np.array([np.array(value) for i in self.landmarks for j in i for value in j])
            tensor_landmark = tf.convert_to_tensor(array_landmark.reshape(-1, 60, 21, 3))
            predict = modelo.predict(tensor_landmark, verbose=0)
            decision = help_predictor.predicts(predict, labels, frame, self.landmarks)

            if decision:
                gesture = decision[0]
                print(f"GESTO DETECTADO = {gesture}")
                self.gesture = gesture
                self.apply_gesture(gesture)  # Aplicar la transformación correspondiente al modelo 3D

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.update_camera_texture(frame)

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
        self.renderer_cam.GetRenderWindow().Render()

    def apply_gesture(self, gesture: str) -> None:
        """
        Aplica la transformación correspondiente al gesto detectado en la cámara 3D.
        """
        cam = self.renderer_stl.GetActiveCamera()
        if gesture == "Displace_Left":
            cam.Azimuth(GESTO_DISPLACE_LEFT)
        elif gesture == "Displace_Right":
            cam.Azimuth(GESTO_DISPLACE_RIGHT)
        elif gesture == "Scroll_Up":
            cam.Elevation(GESTO_SCROLL_UP)
        elif gesture == "Scroll_Down":
            cam.Elevation(GESTO_SCROLL_DOWN)
        elif gesture == "Zoom_In":
            cam.Dolly(GESTO_ZOOM_IN)
            self.renderer_stl.ResetCameraClippingRange()
        elif gesture == "Zoom_Out":
            cam.Dolly(GESTO_ZOOM_OUT)
            self.renderer_stl.ResetCameraClippingRange()

        self.renderer_stl.GetRenderWindow().Render()

# Función principal para cargar el modelo 3D, configurar la ventana y manejar la interacción con la cámara
def lector_vtk():
    # STL
    reader = vtk.vtkSTLReader()
    reader.SetFileName("E:\\PruebasRadiograficas-STL\\RAMIREZ_ACAPANA_TEODORO.stl")
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    # El mapper es responsable de convertir la información 3D del modelo (proporcionada por el lector STL)
    # en datos que pueden ser utilizados por VTK para renderizar la geometría del modelo
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    # El actor es un objeto que tiene el modelo 3D mapeado (con los datos del mapper) y lo puede agregar
    # a un renderizador. Es esencialmente el "objeto" visual que aparece en la escena 3D.   

    # Crear una ventana para renderizar
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(1280, 720)
    # La ventana de renderizado es donde se visualizará todo lo que se renderice.

    # Crear un renderizador para la cámara
    renderer_cam = vtk.vtkRenderer()
    renderer_cam.SetViewport(0.0, 0.0, 0.3, 1.0)
    renderer_cam.SetBackground(0.2, 0.2, 0.2)
    
    # Crear un plano con textura
    planeSource = vtk.vtkPlaneSource()
    planeSource.SetOrigin(1.0, 1.0, 0.0)
    planeSource.SetPoint1(0.0, 1.0, 0.0)
    planeSource.SetPoint2(1.0, 0.0, 0.0)
    planeSource.Update()

    texture = vtk.vtkTexture()
    texture.InterpolateOn()
    
    # Crear un actor para el plano de textura
    mapper_plane = vtk.vtkPolyDataMapper()
    mapper_plane.SetInputConnection(planeSource.GetOutputPort()) 
    # El mapper del plano convierte la geometría generada por el `planeSource` en algo que puede ser visualizado
    actor_plane = vtk.vtkActor()
    actor_plane.SetMapper(mapper_plane)  # Asocia el mapper del plano al actor del plano
    actor_plane.SetTexture(texture)

    renderer_cam.AddActor(actor_plane)  # Agregar el actor del modelo STL al renderizador STL

    # Crear un renderizador para el modelo STL
    renderer_stl = vtk.vtkRenderer()
    renderer_stl.SetViewport(0.3, 0.0, 1.0, 1.0)
    renderer_stl.SetBackground(1.0, 1.0, 1.0)
    renderer_stl.AddActor(actor)

    renderWindow.AddRenderer(renderer_cam)
    renderWindow.AddRenderer(renderer_stl)
    
    # Configurar la captura de video desde la cámara
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Crear el interactor para la ventana de renderizado
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    
    # Establecer el estilo de interacción personalizado con los gestos
    style = GestureInteractorStyle(renderer_stl, actor, renderer_cam, texture, cap)
    style.SetDefaultRenderer(renderer_stl)
    renderWindowInteractor.SetInteractorStyle(style)
    
    # Inicializar y comenzar el bucle de renderizado
    renderWindow.Render()
    renderWindowInteractor.Initialize()
    renderWindowInteractor.CreateRepeatingTimer(1)
    renderWindowInteractor.Start()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    lector_vtk()
