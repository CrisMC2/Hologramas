import vtk

from PyQt5 import QtCore

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class WindowInteractor_Vtk():
    def __init__(self, widget_main: QWidget):
        self.widget = widget_main
        self.vl = QVBoxLayout(self.widget)
        
        self.vtkWidget = QVTKRenderWindowInteractor(self.widget)    

        self.vtkWidget.setAttribute(QtCore.Qt.WA_NativeWindow, True)
        self.vtkWidget.setAttribute(QtCore.Qt.WA_PaintOnScreen, True)
        
        self.vl.addWidget(self.vtkWidget)

        self.renderer = vtk.vtkRenderer()
        self.render_window = self.vtkWidget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)
        # self.vtkWidget.SetRenderWindow(self.render_window)

        self.renderWindowInteractor = self.vtkWidget.GetRenderWindow().GetInteractor()
        
    def set_Style(self, style:vtk.vtkInteractorStyleTrackballCamera,
                    render: vtk.vtkRenderer):
        style.SetDefaultRenderer(render)
        self.renderWindowInteractor.SetInteractorStyle(style)
    
    def render(self):
        self.widget.show()
        self.vtkWidget.Initialize()
        # self.vtkWidget.GetRenderWindow().Render()
        self.render_window.Render()
        self.vtkWidget.Start()