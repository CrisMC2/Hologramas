import os
import sys
import numpy as np
import matplotlib.pyplot as plt
dicoms = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(dicoms)

from DICOM import ViewAxial, ViewSagittal, ViewCoronal, InformationPatient, InformationImage

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QFileDialog, QWidget, QLabel, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from interfaz_actual import Ui_WindowMain

class Main_UI(QMainWindow):
    def __init__(self):
        super(Main_UI, self).__init__()

        #Definimos las clases de otros archivos .py
        self.define_objects()
        
        self.ui = Ui_WindowMain()
        self.ui.setupUi(self)
        
        #Ejecutamos las declaraciones iniciales
        self.declaraciones_iniciales()
        self.connections()
    
    def define_objects(self):
        self.axialView = ViewAxial()
        self.sagittalView = ViewSagittal()
        self.coronalView = ViewCoronal()
        
        self.patientInformation = InformationPatient()
        self.imageInformation = InformationImage()
        
    def declaraciones_iniciales(self):
        #Pantalla inicio
        self.pantalla("Empty")

        #ultima carpeta accedida
        self.carpeta_accedida = "d:"
        
        
        #valor del dicom
        self.value_dicom = 0
        
        #Configuramos la vista del PIXMAP
        self.create_QGraphicsImage()
        self.ui.widget_5.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.ui.widget_7.setAttribute(Qt.WA_TransparentForMouseEvents)
        
    
    def create_QGraphicsImage(self):
        self.one_View_Image = QGraphicsView(self.ui.frame_OneView)
        self.one_View_Image.setGeometry(0, 0, 400, 400)
        
        self.one_View_Image.setDragMode(QGraphicsView.ScrollHandDrag)
        self.one_View_Image.setResizeAnchor(QGraphicsView.AnchorUnderMouse) 
        self.Scene_one_View_Image = QGraphicsScene()
        self.Item_Pixmap = QGraphicsPixmapItem()
        self.one_View_Image.setScene(self.Scene_one_View_Image)
        self.Scene_one_View_Image.addItem(self.Item_Pixmap)
        
        self.Item_Pixmap.setPixmap(QPixmap())
        
        self.one_View_Image.lower()
        
        
        
    #Función de conexiones
    def connections(self):
        #Funciones del Menú de subida
        self.menuUploadFile = self.menu_upload_files()
        self.ui.UploadFiles.setMenu(self.menuUploadFile)
        self.menuUploadFile.triggered.connect(self.upload)
        
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
        self.menuCantViews = self.menu_cant_views()
        self.ui.CantViews.setMenu(self.menuCantViews)
        self.menuCantViews.triggered.connect(self.pantalla)
        
        #Acciones del menú de Cantidad de Vistas
        self.list_actions_menuCantViews = [self.one_view, self.two_view, self.four_view]
        self.one_view.triggered.connect(lambda: self.checkableActions(self.one_view, self.list_actions_menuCantViews))
        self.two_view.triggered.connect(lambda: self.checkableActions(self.two_view, self.list_actions_menuCantViews))
        self.four_view.triggered.connect(lambda: self.checkableActions(self.four_view, self.list_actions_menuCantViews))
        
        
        #Slider para cambiar de imágenes
        self.ui.SliderOneView.valueChanged.connect(self.changeSlider)
        # self.ui.Info_Paciente_2.connect(self.changeText)
        # self.ui.Number_Variable.connect(self.changeText)
        
    def pantalla(self, value: QAction):
        if value=="Empty":
            self.ui.StackedViews.setCurrentWidget(self.ui.EmptyView)
            
        elif value.text() == "1 Vista":
            if self.ui.StackedViews.currentWidget != self.ui.OneView:
                self.ui.StackedViews.setCurrentWidget(self.ui.OneView)
                self.views(self.action_AxialView)
                
        elif value.text()=="2 Vistas":
            if self.ui.StackedViews.currentWidget != self.ui.TwoViews:
                self.ui.StackedViews.setCurrentWidget(self.ui.TwoViews)
        
        elif value.text()=="4 Vistas":
            if self.ui.StackedViews.currentWidget != self.ui.FourViews:
                self.ui.StackedViews.setCurrentWidget(self.ui.FourViews)
            
        
    def menu_upload_files(self):
        menuUploadFiles = QMenu()
        
        UploadFolder = QAction("Upload Folder", self)
        UploadFile = QAction("Upload File", self)
        
        menuUploadFiles.addAction(UploadFolder)
        menuUploadFiles.addAction(UploadFile)
        
        return menuUploadFiles
    
    def menu_cant_views(self):
        menu_cant_views = QMenu()
        
        self.one_view = QAction("1 Vista", self)
        self.two_view = QAction("2 Vistas", self)
        self.four_view = QAction("4 Vistas", self)
        
        #Colocamos a todos como checkable (que tengan el check al lado)
        self.one_view.setCheckable(True)
        self.two_view.setCheckable(True)
        self.four_view.setCheckable(True)
        
        menu_cant_views.addActions([self.one_view, self.two_view, self.four_view])
        return menu_cant_views
        
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
        
    def checkableActions(self, action_use, group_actions):
        for i in group_actions:
            if i == action_use:
                i.setChecked(True)
            else:    
                i.setChecked(False)
                
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
            
            self.array_3D = self.axialView.generate_matriz_dicoms(self.group_Dicoms, -1000, 200)
            
            self.ui.SelectView.setEnabled(True)
            self.ui.CantViews.setEnabled(True)
            
            if len(self.array_3D) == 1:
                self.ui.SliderOneView.hide()
                
            else:
                self.ui.SliderOneView.show()
                self.ui.SliderOneView.setMaximum(len(self.array_3D)-1)
            
            self.changeText(self.ui.name_Patient, self.group_Dicoms[self.value_dicom])
            self.changeText(self.ui.Number_Variable, self.group_Dicoms[self.value_dicom])
            self.checkableActions(self.action_AxialView, self.list_actions_menuViews)
            
            self.pantalla(self.one_view)
            
    def views(self, action):
        if action.text() == "Axial View":
            img = self.axialView.create_view(self.array_3D, self.value_dicom)
            img_QMap = self.create_Pixmap(img)
            self.Item_Pixmap.setPixmap(img_QMap)
            
        elif action.text() == "Sagittal View":
            img = self.sagittalView.create_view(self.array_3D, self.value_dicom)
            img_QMap = self.create_Pixmap(img)
            self.Item_Pixmap.setPixmap(img_QMap)
            
        elif action.text() == "Coronal View":
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
        self.value_dicom = value
        
        for view in self.list_actions_menuViews:
            if view.isChecked():
                self.views(view)
              
        
        self.changeText(self.ui.name_Patient, self.group_Dicoms[self.value_dicom])
        self.changeText(self.ui.Number_Variable, self.group_Dicoms[self.value_dicom])
        
        
    def changeText(self, label: QLabel, dicom_file):
        if label == self.ui.name_Patient:
            label.setText(str(self.patientInformation.get_information(dicom_file, PatientName=True)[0]))
        
        if label == self.ui.Number_Variable:
            label.setText(str(self.imageInformation.get_information(dicom_file, InstanceNumber=True)[0]))
            
        
if __name__ == "__main__":
    app = QApplication([])
    window = Main_UI()
    window.show()
    app.exec_()    