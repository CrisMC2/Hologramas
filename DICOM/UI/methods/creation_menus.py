from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QMenu, QAction, QFileDialog

class Menus(ABC):
    @abstractmethod
    def create_menu(self):
        pass
    
    @abstractmethod
    def connections(self):
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
        
        menuUploadFiles.addAction(self.UploadFolder)
        menuUploadFiles.addAction(self.UploadFile)

        return menuUploadFiles
    
    def connections(self):
        self.UploadFolder.triggered.connect(self.upload_folder)
        self.UploadFile.triggered.connect(self.upload_file)
    
    def upload_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder", self.direction_folder, options=self.options)
        
        if folder_name:
            self.direction_folder = folder_name
        
    def upload_file(self):
        file_name, _ = QFileDialog.getOpenFileNames(self, "Select Files", self.direction_file, "DICOM (*.dcm)", options=self.options)
        
        if file_name:
            if type(file_name) == list:
                self.direction_file = file_name
        
class SelectCantViews(Menus):
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
        self.one_view.triggered.connect(lambda : self.checkable(self.one_view ,self.list_menu_cant_views))
        self.two_view.triggered.connect(lambda : self.checkable(self.two_view ,self.list_menu_cant_views))
        self.four_view.triggered.connect(lambda : self.checkable(self.four_view ,self.list_menu_cant_views))
    
    def checkable(self, action: QAction, list_actions: list):
        for act in list_actions:
            if act == action:
                act.setCheckable(True)
            
            else:
                act.setCheckable(False)
        
class SelectView(Menus):
    def menu_views(self):
        menuViews = QMenu()
        
        self.action_AxialView = QAction("Axial View", self)
        self.action_SaggitalView = QAction("Sagittal View", self)
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
        for act in list_actions:
            if act == action:
                act.setCheckable(True)
            else:
                act.setCheckable(False)