import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from views.viewDICOM import Ui_viewDICOM #Con esta ruta definimos que vista será la elegida

"""
Aquí podemos determinar que vista mostrar.

"""

if __name__ == "__main__":
    app = QApplication(sys.argv) #Agregamos el sys.argv
    main_background = QMainWindow() #Definimos la variable principal con MainWindow
    ui = Ui_viewDICOM() #Instanciamos la vista
    ui.setupUi(main_background) #Ejecutamos la vista
    
    main_background.show() #mostramos
    
    sys.exit(app.exec_()) #En caso de salir, hacemos que sys acabe