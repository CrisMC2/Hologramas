from abc import ABC, abstractmethod
from viewsUI.AbsMenus import AbsMenus

class UploadFiles(ABC, AbsMenus):
    @abstractmethod
    def __upload_folder(self):
        pass

    @abstractmethod 
    def __upload_file(self):
        pass