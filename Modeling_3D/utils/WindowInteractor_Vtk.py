import vtk
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class WindowInteractor_Vtk(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vl = QVBoxLayout()
        
        self.vtkWidget = QVTKRenderWindowInteractor(self)
        self.vl.addWidget(self.vtkWidget)
        self.setLayout(self.vl)

        # self.renderWindowInteractor = self.vtkWidget.GetRenderWindow()
        self.render_window= self.vtkWidget.GetRenderWindow()
        # self.vtkWidget.SetRenderWindow(self.render_window)
        
    def set_Style(self, style:vtk.vtkInteractorStyleTrackballCamera,
                  render: vtk.vtkRenderer):
        style.SetDefaultRenderer(render)
        interactor = self.render_window.GetInteractor()
        interactor.SetInteractorStyle(style)
    
    def render(self):
        self.vtkWidget.Initialize()
        # self.vtkWidget.GetRenderWindow().Render()
        # self.vtkWidget.Start()
        # self.render_window.Render()