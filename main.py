import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow

# from Modeling_3D.Shared.Gesture_Vtk import lector_vtk
# from Modeling_3D.main import execute
from Modeling_3D.controlllers.viewModel3D_Controller import viewModel3D_Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = viewModel3D_Controller(main_window)
    ui.setupUi(main_window)
    main_window.show()
    
    ui.generate_interactor("E:\\UNCP\\SEMILLEROS\\PROYECTO\\PRUEBAS\\MODELOS\\VILCAPOMA QUINTANILLA URSULA.stl")
    cap = cv2.VideoCapture(1)
    ui.show_video(cap)
    
    sys.exit(app.exec_())
    
            
        # self.recept_gest = EmitGest()
        
        # self.recept_gest.execute()
        # self.recept_gest.obj_emit.obj_signal_2.connect(self.on_signal)