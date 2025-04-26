import sys
import os

uiDicom = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(uiDicom)

from controllers import viewDicomController #Importamos todo el archivo, no solo una clase

# """
# Cuando testeamos solo un controlador, no necesitamos importar una ventana principal (QtWidgets)
# para luego instanciar la clase de ui y luego ejecutar setupUi con la ventana principal.

# Solo hace falta iniciar la app mediante sys, instanciar la ventana del Controlador y terminar el sys.

# """
if __name__ == "__main__":
    app = viewDicomController.QApplication(sys.argv)
    view = viewDicomController.Ui_viewDicomController() #Generamos una instancia
    window = view #Como la clase deriva de QMainWindow
    ui = view.ui #Extraemos la viewDICOM
    ui.setupUi(window) #Ejecutamos el inicio de la view
    
    window.show() #Mostramos la vista
    # ui.setup(window)
    
    sys.exit(app.exec_())