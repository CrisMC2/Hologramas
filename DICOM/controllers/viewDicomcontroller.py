import os
import sys
import numpy as np
import matplotlib.pyplot as plt

application = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(application)

from Hologramas.DICOM.core.views.AbsMenus import Upload_Files, SelectCantViews

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QFileDialog, QWidget, QLabel, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from application.interfaz_actual import Ui_WindowMain

class Main_UI(QMainWindow, Ui_WindowMain):
    def __init__(self):
        super(Main_UI, self).__init__()

        self.ui = Ui_WindowMain()
        self.ui.setupUi(self)
        
        #Definimos las clases de otros archivos .py
        self.define_objects()
        
        #Ejecutamos las declaraciones iniciales
        self.declaraciones_iniciales()
        self.connections()
    
    def define_objects(self):
        # self.axialView = ViewAxial()
        # self.sagittalView = ViewSagittal()
        # self.coronalView = ViewCoronal()
        
        # self.patientInformation = InformationPatient()
        # self.imageInformation = InformationImage()
        
        self.upload_file = Upload_Files()
        self.select_cant_views = SelectCantViews()
    
    def declaraciones_iniciales(self):
        #Pantalla inicio
        self.pantalla("Empty")

        #ultima carpeta accedida
        self.carpeta_accedida = "d:"
        
        
        #valor del dicom
        self.value_dicom = 0             

    #Función de conexiones
    def connections(self):
        #Funciones del Menú de subida
        self.menuUploadFile = self.upload_file.create_menu()
        self.upload_file.connections()
        self.ui.UploadFiles.setMenu(self.menuUploadFile)
        
        
        #Funciones del Menú de vistas
        self.menuViews = self.menu_views()
        self.ui.SelectView.setMenu(self.menuViews)
        self.menuViews.triggered.connect(self.views)
        
        #Acciones del menú de Vistas
        self.list_actions_menuViews = [self.action_AxialView, self.action_SagittalView, self.action_CoronalView]
        self.action_AxialView.triggered.connect(lambda: self.checkableActions(self.action_AxialView, self.list_actions_menuViews))
        self.action_SagittalView.triggered.connect(lambda: self.checkableActions(self.action_SagittalView, self.list_actions_menuViews))
        self.action_CoronalView.triggered.connect(lambda: self.checkableActions(self.action_CoronalView, self.list_actions_menuViews))
        
        #Funciones del Menú de Cantidad de Vistas
        self.menuCantViews = self.select_cant_views.create_menu()
        self.select_cant_views.connections(self.ui.StackedViews)
        self.ui.CantViews.setMenu(self.menuCantViews)
        
        #Slider para cambiar de imágenes
        self.ui.SliderOneView.valueChanged.connect(self.changeSlider)
        # self.ui.Info_Paciente_2.connect(self.changeText)
        # self.ui.Number_Variable.connect(self.changeText)
        
    def menu_views(self):
        menuViews = QMenu()
        
        self.action_AxialView = QAction("Axial View", self)
        self.action_SagittalView = QAction("Sagittal View", self)
        self.action_CoronalView = QAction("Coronal View", self)
        
        #Colocamos a todos como checkable
        self.action_AxialView.setCheckable(True)
        self.action_SagittalView.setCheckable(True)
        self.action_CoronalView.setCheckable(True)
        
        menuViews.addActions([self.action_AxialView, self.action_SagittalView, self.action_CoronalView])
        
        return menuViews
         
    def upload (self, action):
        option_file_dialog = QFileDialog.Options()
        
        if action.text() == "Upload Folder":
            self.file_name = QFileDialog.getExistingDirectory(self, "Folder DICOM", self.carpeta_accedida, options=option_file_dialog)
            self.carpeta_accedida = self.file_name
            
        elif action.text() == "Upload File":
            self.file_name, _ = QFileDialog.getOpenFileNames(self, "DICOM Files", self.carpeta_accedida, "Dicom (*.dcm)", options=option_file_dialog)
            if len(self.file_name) > 1:
                self.carpeta_accedida = os.sep.join((self.file_name[0].split(os.sep))[:-1])
            
        if self.file_name:
            if type(self.file_name) == str:
                self.group_Dicoms = self.axialView.extract_multi_dicoms(self.file_name)
                
            elif type(self.file_name) == list:
                self.group_Dicoms = self.axialView.extract_some_dicoms(self.file_name)
            
            self.array_3D = self.axialView.generate_matriz_dicoms(self.group_Dicoms, -200, 200)
            print(self.array_3D.shape)
            self.ui.SelectView.setEnabled(True)
            self.ui.CantViews.setEnabled(True)
            
            if len(self.array_3D) == 1:
                self.ui.SliderOneView.hide()
                
            else:
                self.ui.SliderOneView.show()
            
            self.changeText(self.ui.name_Patient, self.group_Dicoms[0])
            self.changeText(self.ui.Number_Variable, self.array_3D.shape[0])
            self.checkableActions(self.action_AxialView, self.list_actions_menuViews)
            
            self.pantalla(self.one_view)
            
    def views(self, action):
        if action.text() == "Axial View":
            if self.ui.SliderOneView.maximum() != self.array_3D.shape[0]-1:
                self.ui.SliderOneView.setMaximum(self.array_3D.shape[0]-1)
                self.value_dicom = (self.ui.SliderOneView.value())
            
            img = self.axialView.create_view(self.array_3D, self.value_dicom)
            img_QMap = self.create_Pixmap(img)
            self.Item_Pixmap.setPixmap(img_QMap)
            
        elif action.text() == "Sagittal View":
            if self.ui.SliderOneView.maximum() != self.array_3D.shape[1]-1:
                self.ui.SliderOneView.setMaximum(self.array_3D.shape[1]-1)
                self.value_dicom=(self.ui.SliderOneView.value())
            
            print("Saggital View")
            img = self.sagittalView.create_view(self.array_3D, self.value_dicom)
            img_QMap = self.create_Pixmap(img)
            self.Item_Pixmap.setPixmap(img_QMap)
            
        elif action.text() == "Coronal View":
            if self.ui.SliderOneView.maximum() != self.array_3D.shape[2]-1:
                self.ui.SliderOneView.setMaximum(self.array_3D.shape[2]-1)
                self.value_dicom=(self.ui.SliderOneView.value())
            
            img = self.coronalView.create_view(self.array_3D, self.value_dicom)
            img_QMap = self.create_Pixmap(img)
            self.Item_Pixmap.setPixmap(img_QMap)
        
        self.one_View_Image.fitInView(self.Item_Pixmap, Qt.KeepAspectRatio)
          
    def create_Pixmap(self, img: np.uint8):    
        if img.dtype != np.uint8:
            img = img.astype(np.uint8)
        
        #Es necesario que la imagen sea continua (propiedad de QPixmap)
        if not img.flags['C_CONTIGUOUS']:
            img = np.ascontiguousarray(img)
     
        img_QMap = QImage(img, img.shape[0], img.shape[1], img.strides[0],QImage.Format_Grayscale8)
        img_QMap = QPixmap.fromImage(img_QMap)
        
        # tempo = self.ui.view_oneView_2.size()
        # img_QMap = img_QMap.scaled(tempo, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        return img_QMap
    
    def changeSlider(self, value):  
        print(value)
        self.value_dicom = self.ui.SliderOneView.maximum()-value
        print(self.value_dicom)
        
        for view in self.list_actions_menuViews:
            if view.isChecked():
                self.views(view)
        
        # self.changeText(self.ui.name_Patient, dicom_file=self.group_Dicoms[0])
        self.changeText(self.ui.Number_Variable, value=value)
        
        
    def changeText(self, label: QLabel, dicom_file = None, value = None):
        if label == self.ui.name_Patient:
            if dicom_file:
                label.setText(str(self.patientInformation.get_information(dicom_file, PatientName=True)[0]))
        
        if label == self.ui.Number_Variable:
           label.setText(str(value))
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindowMain = QtWidgets.QWidget()
    ui = Main_UI()
    ui.setupUi(WindowMain)
    WindowMain.show()
    sys.exit(app.exec_())