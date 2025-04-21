import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from controllers import viewDicomController as vDcmC #Con esta ruta definimos que vista será la elegida

"""
Aquí podemos determinar que vista mostrar.

"""

if __name__ == "__main__":
    app = vDcmC.QApplication(sys.argv) #Agregamos el sys.argv
    # main_background = QMainWindow() #Definimos la variable principal con MainWindow
    ui = vDcmC.Ui_viewDicomController() #Instanciamos la vista
    # ui.setupUi(main_background) #Ejecutamos la vista
    
    # main_background.show() #mostramos
    ui.show() #Podemos hacer esto porque el controlador deriva de QMainWindow()    
    sys.exit(app.exec_()) #En caso de salir, hacemos que sys acabe