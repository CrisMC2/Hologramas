import sys
import os

view_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(view_append)

#NOTA => Podemos hacer importaciones generales para QApplication o QMainWindow, siempre en cuando estas estén 
    # en la misma versión que está usando la interfaz (Si la UI usa PyQt5, debes importar PyQt5; y si es con PySide6 lo mismo)
    #   Por ello, y para evitar posibles futuros errores es mejor directamente importar estos elementos desde el mismo archivo de la UI
# from PyQt5.QtWidgets import QApplication, QMainWindow

from views import viewDICOM

if __name__ == "__main__":
    app = viewDICOM.QtWidgets.QApplication(sys.argv)
    main_background = viewDICOM.QtWidgets.QMainWindow()
    ui = viewDICOM.Ui_viewDICOM()
    
    ui.setupUi(main_background) #setupUI necesita de una ventana principal en la cual se alojará toda la interfaz
    main_background.show()
    
    sys.exit(app.exec_())