import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from controllers.viewDicomController import Ui_viewDicomController #Con esta ruta definimos que vista será la elegida

"""
Aquí podemos determinar que vista mostrar.

"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_viewDicomController()
    
    window.setCentralWidget(ui.widget_main)
    
    window.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     app = vDcmC.QApplication(sys.argv) #Agregamos el sys.argv
#     view = vDcmC.Ui_viewDicomController() #Instanciamos la vista
    
#     main_window = view
#     ui = view.ui
    
#     ui.setupUi(main_window)
#     view.setupUiController()
#     # ui.setupUi(main_background) #Ejecutamos la vista
    
#     # main_background.show() #mostramos
#     main_window.show() #Podemos hacer esto porque el controlador deriva de QMainWindow()    
#     sys.exit(app.exec_()) #En caso de salir, hacemos que sys acabe  