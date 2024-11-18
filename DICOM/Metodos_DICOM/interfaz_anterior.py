import PySide6.QtGui
from DICOM import DicomConvert3D, DicomConvertVideo,DicomConvertNifti, DicomConvertImage, InformationImage, InformationStudySerie, InformationPatient, ViewAxial, ViewCoronal, ViewSagittal
import PySide6
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QPixmap, QImage
import numpy as np
import matplotlib.pyplot as plt
import cv2

# PySide6.QtCore.QCoreApplication.setAttribute(PySide6.QtCore.Qt.AA_ShareOpenGLContexts)
class Observer():
    def __init__(self, initial_value=0):
        self._value = initial_value
        self.list_Observer = []
        
    def add_Observer(self, function):
        self.list_Observer.append(function)
    
    def set_value(self, value):
        if self._value != value:
            self._value = value
            self.notify_observer()
    
    def get_value(self):
        return self._value
    
    def notify_observer(self):
        for observer in self.list_Observer:
            observer(self._value)
        
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Cargar el archivo .ui
        ui_file = QFile("UI_Mostrar_Views.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        
        self.observerSlider = Observer()
        self.observerSlider.add_Observer(self.actualizar_view)
        
        self.axial = ViewAxial()
        self.sagittal = ViewSagittal()
        self.coronal = ViewCoronal()
        
        self.ui.BtnLoadElement.clicked.connect(self.BtnLoadElement_clicked)
        self.ui.BtnLoadDataset.clicked.connect(self.BtnLoadDataset_clicked)
        self.ui.BtnConvertPng.clicked.connect(self.BtnConvertPng_clicked)
        self.ui.BtnConvertVideo.clicked.connect(self.BtnConvertVideo_clicked)
        self.ui.SliderDicom.valueChanged.connect(self.SliderDicom_scroll)      
        self.ui.label_slice.setText("Valor del Slider")       
         
    def BtnLoadElement_clicked(self):
        print("Load Element")   
        path_element = self.select_file()
        
    
    def BtnLoadDataset_clicked(self):
        print("Load Dataset")
        self.path_folder = self.select_folder()
        self.mostrar_view(self.path_folder)
    
    def BtnConvertPng_clicked(self):
        print("Conver Png")
    
    def BtnConvertVideo_clicked(self):
        print("Convert Video")
        
    def SliderDicom_scroll(self, value):
        self.observerSlider.set_value(value)
        self.ui.label_slice.setText(str(value))
    
    def select_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly  # Solo lectura
        file_name, _ = QtWidgets.QFileDialog.getOpenFileUrl(self, "Selecciona un archivo", "", "Todos los archivos (*);;Archivos dicom (*.dcm)", options=options)

        if file_name:
            # print(f"Archivo seleccionado: {file_name}")  # Muestra la ruta del archivo en la consola
            # Aquí puedes añadir lógica para trabajar con el archivo seleccionado
            return file_name

    def select_folder(self):
        carpeta = QtWidgets.QFileDialog.getExistingDirectory(None, "Selecciona una carpeta")
        if carpeta:
            print("Carpeta seleccionada:", carpeta)
        else:
            print("No se seleccionó ninguna carpeta")
        
        return carpeta
        
    def image_label(self, img_axial: np.uint8, img_sagittal: np.uint8, img_coronal: np.uint8):
        if img_axial.dtype != np.uint8:
            img_axial = img_axial.astype(np.uint8)
            print("Imagen axial convertida a uint8")
        
        if img_sagittal.dtype != np.uint8:
            img_sagittal = img_sagittal.astype(np.uint8)
            print("Imagen sagital convertida a uint8")
            
            
        if img_coronal.dtype != np.uint8:
            img_coronal = img_coronal.astype(np.uint8)
            print("Imagen coronal convertida a uint8")
            
        if not img_axial.flags['C_CONTIGUOUS']:
            img_axial = np.ascontiguousarray(img_axial)
            print("Cnnvertido a constante")
        
        if not img_sagittal.flags['C_CONTIGUOUS']:
            img_sagittal = np.ascontiguousarray(img_sagittal)
        
        if not img_coronal.flags['C_CONTIGUOUS']:
            img_coronal = np.ascontiguousarray(img_coronal)
        
        qimage_axial = QImage(img_axial, img_axial.shape[0],img_axial.shape[1], QImage.Format_Grayscale8)
        qimage_sagittal = QImage(img_sagittal, img_sagittal.shape[0],img_sagittal.shape[1], img_sagittal.strides[0], QImage.Format_Grayscale8)
        qimage_coronal = QImage(img_coronal, img_coronal.shape[0],img_coronal.shape[1], img_coronal.strides[0], QImage.Format_Grayscale8)
        
        # Convertir QImage a QPixmap y asignarlo al QLabel
        pixmap_axial = QPixmap.fromImage(qimage_axial)
        pixmap_sagittal = QPixmap.fromImage(qimage_sagittal)
        pixmap_coronal = QPixmap.fromImage(qimage_coronal)
        
        
        # Obtener el tamaño del QLabel
        axial_size = self.ui.axial_label.size()
        sagittal_size = self.ui.sagittal_label.size()
        coronal_size = self.ui.coronal_label.size()

        # Redimensionar el pixmap al tamaño del QLabel
        pixmap_axial = pixmap_axial.scaled(axial_size, Qt.KeepAspectRatio, Qt.SmoothTransformation,)
        pixmap_sagittal = pixmap_sagittal.scaled(sagittal_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pixmap_coronal = pixmap_coronal.scaled(coronal_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.ui.axial_label.setPixmap(pixmap_axial)
        self.ui.sagittal_label.setPixmap(pixmap_sagittal)
        self.ui.coronal_label.setPixmap(pixmap_coronal)
        
            
        
    def mostrar_view(self, path_folder):
        #Elegimos cualquier método para crear la matriz de dicoms
        self.matriz_3D = self.axial.create_matriz_dicoms(path_folder, -200, 200)
        self.ui.SliderDicom.setMaximum(self.matriz_3D.shape[2]-1)
        
        img_axial = self.axial.create_view(self.matriz_3D, 0)
        img_sagittal = self.sagittal.create_view(self.matriz_3D, 0)
        img_coronal = self.coronal.create_view(self.matriz_3D, 0)

        self.image_label(img_axial, img_sagittal, img_coronal)
    
    def actualizar_view(self, value):
        img_axial = self.axial.create_view(self.matriz_3D, value)
        img_sagittal = self.sagittal.create_view(self.matriz_3D, value)
        img_coronal = self.coronal.create_view(self.matriz_3D, value)
        
        self.image_label(img_axial, img_sagittal, img_coronal)
        
        

if __name__ == '__main__':    
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
