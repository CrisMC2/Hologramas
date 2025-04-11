import os
import sys

append_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(append_folder)

from PyQt5.QtWidgets import QFileDialog, QMenu, QAction
from abstracts.Ui.AbsMenus import AbsMenus
from abstracts.Ui.AbsActions import AbsActions
from abstracts.Ui.AbsUploadData import AbsUploadData
from utils.SignalData import Emisor_text, Emisor_list

class MenuUploadFiles(AbsMenus, AbsActions):
    """
    
    """    
    
    def __init__(self, directory_search_default: str, type_file_filter: str, keep_directory_default: bool = False):
        super().__init__()
        
        self.obj_folder_uploader = FolderUploader(directory_search_default= directory_search_default, 
                                                   type_file_filter= type_file_filter, 
                                                   keep_directory_initial= keep_directory_default) #Instanciamos la búsqueda de "FOLDER"
        self.obj_file_uploader = FileUploader(directory_search_default= directory_search_default, 
                                               type_file_filter= type_file_filter, 
                                               keep_directory_initial= keep_directory_default)  #Instanciamos la búsqueda de "FILE"
        
        self.emisor_text = Emisor_text() #Instancias la clase que nos permitirá emitir la señal
        self.emisor_list = Emisor_list()
    
    #Herencia de AbsMenus
    def create_menu(self):
        menuUploadFiles = QMenu()
        self.create_actions()
        self.check_action(self.list_actions)
        self.connections()
        
        menuUploadFiles.addActions(self.list_actions)
        return menuUploadFiles

    #Herencia de AbsActions
    def create_actions(self):
        self.act_upload_folder = QAction("Upload Folder", self)
        self.act_upload_file = QAction("Upload File", self)
        
        self.list_actions = [self.act_upload_folder, self.act_upload_file]
    
    #Herencia de AbsMenus
    def connections(self):
        self.act_upload_folder.triggered.connect(self.obj_folder_uploader.upload)
        self.act_upload_file.triggered.connect(self.obj_file_uploader.upload)
        
        self.act_upload_folder.triggered.connect(lambda : self.toggle_check_action(self.act_upload_folder, self.list_actions))
        self.act_upload_file.triggered.connect(lambda : self.toggle_check_action(self.act_upload_file, self.list_actions))
        
        self.act_upload_folder.triggered.connect(self.get_path)
        self.act_upload_file.triggered.connect(self.get_path)

    #Herencia de AbsMenus
    def enable_menu(self, enable: bool, menu: QMenu):
        super().enable_menu(enable, menu)
        
    #Herencia de AbsActions
    def check_action(self, list_actions: list[QAction]):
        for action in list_actions:
            action.setCheckable(True)
            
    #Herencia de AbsActions
    def toggle_check_action(self, action: QAction, list_actions: list[QAction]):
        super().toggle_check_action(action, list_actions)
        
    """
    El método get_path está pensado para que se devuelva la dirección 
    """
    def get_path(self):
        folder = self.obj_folder_uploader.get_directory()
        files = self.obj_file_uploader.get_directory()
        
        if folder:
            self.emisor_text.emit_signal(folder)
        elif files:
            self.emisor_list.emit_signal(files)
    
    
    
class FolderUploader(AbsUploadData):
    def __init__(self, directory_search_default: str, type_file_filter: str, keep_directory_initial: bool = False):
        super().__init__()
        
        self.directory_search = directory_search_default
        self.type_file_filter = type_file_filter
        self.keep_directory_initial = keep_directory_initial
        
        self.directory_selected = "" #Es el directorio seleccionado actualmente
        
        self.options = QFileDialog.Options()
    """
    El método permite seleccionar una carpeta mediante una ventana "modal".
    
    - El método abre una ventana la cuál permitirá acceder a los archivos.
    - La ventana solo permitirá seleccionar carpetas, mas no archivos directamente.
    
    - El método analiza si se selecciono una carpeta o no.
    - El método permite mantener o no la dirección inicial dada en self.directory_search. 
                Siendo su cambio (Si se permite) a la última dirección accedida por el usuario.
    
    - Parámetros:
        - self (FileUploader)   : Instancia de la clase FileUploader.
        
    - Retorno:
        - void (vacío)  : El método directamente no retorna ningún valor, 
                            lo que realiza es asignarle un valor a una variable de clase (self.directory_selected).
    """
    #Herencia de AbsUploadData
    def upload(self):
        self.folder_name = QFileDialog.getExistingDirectory(self, "Select Folder", self.directory_search, options=self.options)
        
        if self.folder_name:
            self.directory_selected = self.folder_name
            print("Directorio: "+self.folder_name)
            if not self.keep_directory_initial:
                self.directory_search = self.folder_name
            
    """
    El siguiente método permite retornar el directorio que previamente ha sido seleccionado.
    
    - El método toma una copia de la variable self.directory_selected.
    - Se limpia en cada retorno la variable self.directory_selected con la intención de no repetir una dirección que no haya sido 
        seleccionada previamente.
    
    - Parámetros:
        - self (FileUploader)   : Instancia de la clase FileUploader.
        
    - Retorno:
        - directory (str)       : Directorio seleccionado.
    """
    #Herencia de AbsUploadData
    def get_directory(self):
        if self.directory_selected != "":
            directory = self.directory_selected
            
            self.clean_directory(self.directory_selected) # de esta manera evitamos que el directorio anteriormente abierto lo haga de nuevo.
            
            return directory
        
        return None
    
    """
    El método permite limpiar una dirección.
    
    - Ello involucrado limpiar la variable string por medio de volverlo un archivo vacío.

    - Parámetros:
        - self (FileUploader)   : Instancia de la clase FileUploader
        - directory (str)       : Dirección del file.
        
    - Retorno:
        -void       : el método es vacío, no tiene retorno.
    """
    #Herencia de AbsUploadData
    def clean_directory(self, directory: str):
        if directory != "":
            directory = ""
        else: 
            print("El directorio ya está vacío.")







"""
Esta clase nos permite poder acceder a los archivos del sistema y 
extraer un archivo del formato u extensión que se desee.
"""
class FileUploader(AbsUploadData):
    def __init__(self, directory_search_default: str, type_file_filter: str, keep_directory_initial: bool = False):
        super().__init__()
        
        self.directory_search = directory_search_default        
        self.type_file_filter = type_file_filter
        self.keep_directory_initial = keep_directory_initial
        
        self.list_directory = list() #Es la cantidad de directorios seleccionados actualmente
        
        self.option = QFileDialog.Options()
    
    """
    El método permite seleccionar uno o múltiples direcciones
    """
    #Herencia de AbsUploadData
    def upload(self):
        file_name, _ = QFileDialog.getOpenFileNames(self, "Select to file", 
                                                         self.directory_search, self.type_file_filter, options= self.option)
        if file_name:
            self.list_directory = file_name
            
            if not self.keep_directory_initial:
                self.directory_search = os.path.dirname(file_name[0])
                # self.direction_file = (os.path.join((self.file_name[0].split(os.sep))[:-1])) 
                # self.direction_file = os.path.splitext(self.file_name[0])[0] #El método separa una dirección de su extensión
    
    
    """
    El siguiente método permite retornar el directorio que previamente ha sido seleccionado.
    
    - El método toma una copia de la variable self.directory_selected.
    - Se limpia en cada retorno la variable self.directory_selected con la intención de no repetir una dirección que no haya sido 
        seleccionada previamente.
    
    - Parámetros:
        - self (FileUploader)   : Instancia de la clase FileUploader.
        
    - Retorno:
        - directory (list)       : Lista de directorios seleccionados.
        
    """
    #Herencia de AbsUploadData
    def get_directory(self):
        if len(self.list_directory):
            list_copy = self.list_directory.copy()
            self.clean_directory(self.list_directory)
        
            return list_copy
        return None
    
    #Herencia de AbsUploadData
    def clean_directory(self, list_directory: list[str]):
        if len(list_directory):
            list_directory.clear()
        else:
            print("El directorio ya está vacío.")