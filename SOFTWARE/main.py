# Archivo principal para ejecutar la aplicación con PyQt
# Importamos los módulos necesarios desde el archivo `interfazz.py`
from Views.interfazz import QtWidgets, Ui_fondoMain 
#from metodos import setup_connections

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fondoMain = QtWidgets.QMainWindow()
    ui = Ui_fondoMain()
    ui.setupUi(fondoMain)
    fondoMain.show()
    #ui.setup_connections()
    sys.exit(app.exec_())