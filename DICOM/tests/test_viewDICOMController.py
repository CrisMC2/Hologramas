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
    window = viewDicomController.Ui_DicomController()
    window.show()
    
    sys.exit(app.exec_())