import sys
from PyQt5.QtWidgets import QApplication

# from Modeling_3D.Shared.Gesture_Vtk import lector_vtk
from Modeling_3D.main import execute

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # lector_vtk("E:\\UNCP\\SEMILLEROS\\PROYECTO\\PRUEBAS\\MODELOS\\VILCAPOMA QUINTANILLA URSULA.stl")
    main_window = execute("E:\\UNCP\\SEMILLEROS\\PROYECTO\\PRUEBAS\\MODELOS\\VILCAPOMA QUINTANILLA URSULA.stl")
    
    sys.exit(app.exec_())
    
            
        # self.recept_gest = EmitGest()
        
        # self.recept_gest.execute()
        # self.recept_gest.obj_emit.obj_signal_2.connect(self.on_signal)