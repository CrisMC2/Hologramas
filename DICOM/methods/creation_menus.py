import os
import sys
import numpy as np

from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QMenu, QAction, QFileDialog, QStackedWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap

dicoms = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(dicoms)

from Metodos_DICOM.DICOM import ViewAxial, ViewSagittal, ViewCoronal, InformationPatient, InformationImage

class Menus(ABC):
    @abstractmethod
    def create_menu(self):
        pass
    
    @abstractmethod
    def connections(self):
        pass

class ImageUI(ABC):
    @abstractmethod
    def create_pixmap(self):
        pass
    @abstractmethod
    def set_image(self):
        pass    

class Upload_Files(Menus):
    def __init__(self):
        self.direction_folder = 'c:'
        self.direction_file = 'c:'
        self.options = QFileDialog.Options()
        
    def create_menu(self):
        menuUploadFiles = QMenu()
        
        self.UploadFolder = QAction("Upload Folder", self)
        self.UploadFile = QAction("Upload File", self)
        
        menuUploadFiles.addActions([self.UploadFolder, self.UploadFile])
        return menuUploadFiles

    def connections(self):
        self.UploadFolder.triggered.connect(self.__upload_folder)
        self.UploadFile.triggered.connect(self.__upload_file)

    def __upload_folder(self):
        self.folder_name = QFileDialog.getExistingDirectory(self, "Select Folder", self.direction_folder, options=self.options)
        
        if self.folder_name:
            self.direction_folder = self.folder_name
        
    def __upload_file(self):
        self.file_name, _ = QFileDialog.getOpenFileNames(self, "Select Files", self.direction_file, "DICOM (*.dcm)", options=self.options)
        
        if self.file_name:
            if type(self.file_name) == str:
                self.direction_file = self.file_name    
            elif type(self.file_name) == list:
                self.direction_file = (os.path.join((self.file_name[0].split(os.sep))[:-1]))

class SelectCantViews(Menus):
    def __init__(self, stackedWidget: QStackedWidget):
        self.stacked_widget = stackedWidget
    
    def menu_cant_views(self):
        menu_cant_views = QMenu()
        
        self.one_view = QAction("1 View", self)
        self.two_view = QAction("2 Views", self)
        self.four_view = QAction("4 Views", self)
        
        #Colocamos a todos como checkable (que tengan el check al lado)
        self.one_view.setCheckable(True)
        self.two_view.setCheckable(True)
        self.four_view.setCheckable(True)
        
        self.list_menu_cant_views = [self.one_view, self.two_view, self.four_view]
        menu_cant_views.addActions(self.list_menu_cant_views)
        return menu_cant_views

    def connections(self):
        cant_view = self.menu_cant_views()
        cant_view.triggered.connect(lambda : self.checkable(list_actions=self.list_menu_cant_views))
        self.one_view.triggered.connect(lambda : self.checkable(self.one_view, self.list_menu_cant_views))
        self.two_view.triggered.connect(lambda : self.checkable(self.two_view, self.list_menu_cant_views))
        self.four_view.triggered.connect(lambda : self.checkable(self.four_view, self.list_menu_cant_views))
    
    def checkable(self, action: QAction, list_actions: list):
        if action.isChecked():
            for act in list_actions:
                if act == action:
                    act.setCheckable(True)
                else:
                    act.setCheckable(False)
            
            self.stacked_widget.setCurrentWidget(action)
            
class SelectView(Menus, ImageUI):
    def __init__(self):
        self.view = "Axial View"
    def menu_views(self):
        menuViews = QMenu()
        
        self.action_AxialView = QAction("Axial View", self)
        self.action_SaggitalView = QAction("Saggital View", self)
        self.action_CoronalView = QAction("Coronal View", self)
        
        #Colocamos a todos como checkable
        self.action_AxialView.setCheckable(True)
        self.action_SaggitalView.setCheckable(True)
        self.action_CoronalView.setCheckable(True)
        
        self.list_menu_views = [self.action_AxialView, self.action_SaggitalView, self.action_CoronalView]
        menuViews.addActions(self.list_menu_views)
        
        return menuViews
    
    def connections(self):
        self.action_AxialView.triggered.connect(lambda : self.checkable(self.action_AxialView, self.list_menu_views))
        self.action_SaggitalView.triggered.connect(lambda : self.checkable(self.action_SaggitalView, self.list_menu_views))
        self.action_CoronalView.triggered.connect(lambda : self.checkable(self.action_CoronalView, self.list_menu_views))
        
    def checkable(self, action: QAction, list_actions: list):
        if action:
            for act in list_actions:
                if act == action:
                    act.setCheckable(True)
                else:
                    act.setCheckable(False)

            self.view = action.text()
    
class InsertView():
    def __init__(self, label: QLabel):
        self.label = label
        self.axial = ViewAxial()
        self.saggital = ViewSagittal()
        self.coronal = ViewCoronal()
        
    def insert_view(self, view: str = "Axial View"):
        if view == "Axial View":
            # img_array = self.axial.
            pass
        
        elif view == "Saggital View":
            pass
        elif view == "Coronal View":
            pass
    
    def create_pixmap(self, img: np.uint8):
        if img.dtype != np.uint8:
            img = img.astype(np.uint8)
        
        if not img.flags["C_CONTIGUOUS"]:
            img = np.ascontiguousarray(img)
        
        img_pix_map = QImage(img, img.shape[0], img.shape[1], img.strides[1], QImage.Format_Grayscale8)
        img_pix_map = QPixmap.fromImage(img_pix_map)
        
        return img_pix_map
    
    def set_image(self, img: QPixmap, label: QLabel = None):
        if label:
            self.label = label
        
        self.label.setPixmap(img)