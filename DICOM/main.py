import sys

from views import viewDICOM as vDICOM

"""
Aquí podemos determinar que vista mostrar.

"""

if __name__ == "__main__":
    app = vDICOM.QtWidgets.QApplication(sys.argv)
    main_background = vDICOM.QtWidgets.QMainWindow()
    ui = vDICOM.Ui_WindowMain()
    ui.setupUi(main_background)
    
    main_background.show()
    
    sys.exit(app.exec_())