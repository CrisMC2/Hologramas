# 20 FRAMES

import sys
import os
import numpy as np
import tensorflow as tf
import cv2
import vtk
from scipy.interpolate import interp1d
from typing import Optional

# Importar funciones reutilizables
from ejecucion_conv_60 import configurar_rutas, inicializar_componentes

# Configurar rutas
configurar_rutas()

# Cargar modelo, detector de manos y helper
modelo, landmark, help_predictor, labels = inicializar_componentes()

from gesture_settings import (
    GESTO_DISPLACE_LEFT,
    GESTO_DISPLACE_RIGHT,
    GESTO_SCROLL_UP,
    GESTO_SCROLL_DOWN,
    GESTO_ZOOM_IN,
    GESTO_ZOOM_OUT
)
from vtkmodules.vtkCommonCore import vtkOutputWindow

# Clase para ignorar errores de interfaz VTK
class MyVTKOutputWindow(vtkOutputWindow):
    def DisplayText(self, text: str) -> None:
        pass

vtkOutputWindow.SetInstance(MyVTKOutputWindow())

class GestureInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, renderer_stl, actor, renderer_cam, texture, cap):
        self.AddObserver("TimerEvent", self.on_timer)
        self.renderer_stl = renderer_stl
        self.actor = actor
        self.renderer_cam = renderer_cam
        self.texture = texture
        self.cap = cap
        self.gesture = None
        self.landmarks = []

    def interpolar_frames(self, frames: np.ndarray, n_objetivo:int=60):
        frames = np.array(frames)
        n_actual = frames.shape[0]
        x_actual = np.linspace(0, 1, n_actual)
        x_nuevo = np.linspace(0, 1, n_objetivo)

        interpolado = np.zeros((n_objetivo, 21, 3))
        for i in range(21):
            for j in range(3):
                f = interp1d(x_actual, frames[:, i, j], kind='linear')
                interpolado[:, i, j] = f(x_nuevo)
        return interpolado

    def on_timer(self, obj, event):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = landmark.drawHands(frame, True)
        self.landmarks = landmark.guardar_frames(frame, 20)

        if self.landmarks and len(self.landmarks) == 20:
            interpolado = self.interpolar_frames(self.landmarks, 60)

            if interpolado.shape == (60, 21, 3):
                tensor_landmark = tf.convert_to_tensor(interpolado.reshape(-1, 60, 21, 3))
                predict = modelo.predict(tensor_landmark, verbose=0)
                decision = help_predictor.predicts(predict, labels, frame, self.landmarks)

                if decision:
                    gesture = decision[0]
                    print(f"GESTO DETECTADO = {gesture}")
                    self.gesture = gesture
                    self.apply_gesture(gesture)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.update_camera_texture(frame)

    def update_camera_texture(self, frame):
        h, w, _ = frame.shape
        vtk_image = vtk.vtkImageImport()
        vtk_image.CopyImportVoidPointer(frame.tobytes(), len(frame.tobytes()))
        vtk_image.SetDataScalarTypeToUnsignedChar()
        vtk_image.SetNumberOfScalarComponents(3)
        vtk_image.SetDataExtent(0, w-1, 0, h-1, 0, 0)
        vtk_image.SetWholeExtent(0, w-1, 0, h-1, 0, 0)
        vtk_image.Update()

        self.texture.SetInputConnection(vtk_image.GetOutputPort())
        self.renderer_cam.GetRenderWindow().Render()

    def apply_gesture(self, gesture: str) -> None:
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

def lector_vtk():
    reader = vtk.vtkSTLReader()
    reader.SetFileName("E:\\PruebasRadiograficas-STL\\RAMIREZ_ACAPANA_TEODORO.stl")
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(1280, 720)

    renderer_cam = vtk.vtkRenderer()
    renderer_cam.SetViewport(0.0, 0.0, 0.3, 1.0)
    renderer_cam.SetBackground(0.2, 0.2, 0.2)

    planeSource = vtk.vtkPlaneSource()
    planeSource.SetOrigin(1.0, 1.0, 0.0)
    planeSource.SetPoint1(0.0, 1.0, 0.0)
    planeSource.SetPoint2(1.0, 0.0, 0.0)
    planeSource.Update()

    texture = vtk.vtkTexture()
    texture.InterpolateOn()

    mapper_plane = vtk.vtkPolyDataMapper()
    mapper_plane.SetInputConnection(planeSource.GetOutputPort())

    actor_plane = vtk.vtkActor()
    actor_plane.SetMapper(mapper_plane)
    actor_plane.SetTexture(texture)

    renderer_cam.AddActor(actor_plane)

    renderer_stl = vtk.vtkRenderer()
    renderer_stl.SetViewport(0.3, 0.0, 1.0, 1.0)
    renderer_stl.SetBackground(1.0, 1.0, 1.0)
    renderer_stl.AddActor(actor)

    renderWindow.AddRenderer(renderer_cam)
    renderWindow.AddRenderer(renderer_stl)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    style = GestureInteractorStyle(renderer_stl, actor, renderer_cam, texture, cap)
    style.SetDefaultRenderer(renderer_stl)
    renderWindowInteractor.SetInteractorStyle(style)

    renderWindow.Render()
    renderWindowInteractor.Initialize()
    renderWindowInteractor.CreateRepeatingTimer(10)
    renderWindowInteractor.Start()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    lector_vtk()
