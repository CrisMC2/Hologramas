import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow

# from Modeling_3D.Shared.Gesture_Vtk import lector_vtk
from Modeling_3D.main import execute
# from UI_Dicom.main import execute

if __name__ == "__main__":
    # execute(r"E:\UNCP\SEMILLEROS\PROYECTO\PRUEBAS\MODELOS\VILCAPOMA QUINTANILLA URSULA.stl")
    execute(r"E:/UNCP/SEMILLEROS/PROYECTO/PRUEBAS/MODELOS/VILCAPOMA QUINTANILLA URSULA.stl")
    
            
        # self.recept_gest = EmitGest()
        
        # self.recept_gest.execute()
        # self.recept_gest.obj_emit.obj_signal_2.connect(self.on_signal)