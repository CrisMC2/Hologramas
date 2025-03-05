# Interfaz de views, etc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QListWidget, QVBoxLayout, QWidget, QMessageBox, QLineEdit, QListWidgetItem
from Gmail import enviar_codigo_verificacion, verificar_codigo
from PyQt5.QtCore import QTimer
from conexion import *
from conexion import obtener_guardados
from PyQt5.QtCore import Qt

class Ui_fondoMain(object):

   def setupUi(self, fondoMain):
        fondoMain.setObjectName("fondoMain")
        fondoMain.resize(1927, 1080) 
        self.centralwidget = QtWidgets.QWidget(fondoMain)
        self.centralwidget.setObjectName("centralwidget")
        self.cambianteTodo = QtWidgets.QStackedWidget(self.centralwidget)
        self.cambianteTodo.setGeometry(QtCore.QRect(-20, 0, 1951, 1021))
        self.cambianteTodo.setStyleSheet("background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #a7a7a7, stop:1 #d2d2d2)")
        self.cambianteTodo.setObjectName("cambianteTodo")

        self.ensayo = QtWidgets.QWidget()
        self.ensayo.setObjectName("ensayo")
        self.label_433 = QtWidgets.QLabel(self.ensayo)
        self.label_433.setGeometry(QtCore.QRect(270, 60, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_433.setFont(font)
        self.label_433.setStyleSheet("QLabel {\n"
"    color: black; /* Cambia #3498db por el color que prefieras */\n"
"    background:none;\n"
"}")
        self.label_433.setObjectName("label_433")
        self.widget_127 = QtWidgets.QWidget(self.ensayo)
        self.widget_127.setGeometry(QtCore.QRect(750, 30, 1131, 131))
        self.widget_127.setStyleSheet("border-radius: 30px; /* Ajusta el valor para el radio de los bordes */\n"
"background-color:#242525;\n"
"border: none;            /* Borde negro */\n"
"border-radius: 20px;")
        self.widget_127.setObjectName("widget_127")
        self.label_434 = QtWidgets.QLabel(self.widget_127)
        self.label_434.setGeometry(QtCore.QRect(40, 47, 371, 31))
        self.label_434.setStyleSheet("background: transparent;\n"
"border: none;")
        self.label_434.setObjectName("label_434")
        self.label_435 = QtWidgets.QLabel(self.widget_127)
        self.label_435.setGeometry(QtCore.QRect(450, 30, 101, 71))
        self.label_435.setStyleSheet("border: none;")
        self.label_435.setText("")
        self.label_435.setPixmap(QtGui.QPixmap("E:/6TO SEMESTRE/C:/6TO_SEMESTRE/Hologramas/icon/an-indian-young-female-doctor-isolated-on-green-ai-generated-photo.jpg"))
        self.label_435.setScaledContents(True)
        self.label_435.setObjectName("label_435")
        self.label_436 = QtWidgets.QLabel(self.widget_127)
        self.label_436.setGeometry(QtCore.QRect(570, 37, 231, 51))
        self.label_436.setStyleSheet("background: transparent;\n"
"border: none;")
        self.label_436.setObjectName("label_436")
        self.pushButton_230 = QtWidgets.QPushButton(self.widget_127)
        self.pushButton_230.setGeometry(QtCore.QRect(850, 40, 131, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_230.setFont(font)
        self.pushButton_230.setMouseTracking(False)
        self.pushButton_230.setStyleSheet("QPushButton {\n"
"    background-color: #e92030;  /* Fondo transparente */\n"
"    border: none;              /* Borde blanco */\n"
"    border-radius: 18px;                  /* Bordes redondeados */\n"
"    color:  white;                         /* Color del texto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_230.setObjectName("pushButton_230")
        self.Boton_Atras_70 = QtWidgets.QPushButton(self.widget_127)
        self.Boton_Atras_70.setGeometry(QtCore.QRect(1000, 40, 61, 41))
        self.Boton_Atras_70.setStyleSheet("QPushButton {\n"
"    background-position: center;    /* Centrar la imagen */\n"
"    background-size: contain;\n"
"    background-color: transparent;    /* Cambiar el tamaño de la imagen (ajusta según sea necesario) */\n"
"    border: none;                   /* Elimina el borde del botón */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Color de fondo cuando el mouse está sobre el botón */\n"
"    color: white;               /* Color del texto al hacer hover */\n"
"    border: none;  /* Cambiar el color del borde al hacer hover */\n"
"}")
        self.Boton_Atras_70.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Boton_Atras_70.setIcon(icon3)
        self.Boton_Atras_70.setIconSize(QtCore.QSize(70, 70))
        self.Boton_Atras_70.setObjectName("Boton_Atras_70")
        self.widget_25 = QtWidgets.QWidget(self.ensayo)
        self.widget_25.setGeometry(QtCore.QRect(240, 190, 1651, 751))
        self.widget_25.setStyleSheet("border-radius: 30px; /* Ajusta el valor para el radio de los bordes */\n"
"background-color:#242525;\n"
"border: none;            /* Borde negro */\n"
"border-radius: 20px;")
        self.widget_25.setObjectName("widget_25")
        self.widget_128 = QtWidgets.QWidget(self.widget_25)
        self.widget_128.setGeometry(QtCore.QRect(1160, 630, 451, 61))
        self.widget_128.setStyleSheet("border-radius: 30px; /* Ajusta el valor para el radio de los bordes */\n"
"background-color:black;\n"
"border: none;            /* Borde negro */\n"
"border-radius: 20px;")
        self.widget_128.setObjectName("widget_128")
        self.label_437 = QtWidgets.QLabel(self.widget_128)
        self.label_437.setGeometry(QtCore.QRect(50, 10, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_437.setFont(font)
        self.label_437.setStyleSheet("QLabel {\n"
"    color: black; /* Cambia #3498db por el color que prefieras */\n"
"    background:none;\n"
"}")
        self.label_437.setObjectName("label_437")
        self.label_438 = QtWidgets.QLabel(self.widget_25)
        self.label_438.setGeometry(QtCore.QRect(1160, 30, 121, 31))
        self.label_438.setStyleSheet("background: transparent;\n"
"border: none;")
        self.label_438.setObjectName("label_438")
        self.widget_129 = QtWidgets.QWidget(self.widget_25)
        self.widget_129.setGeometry(QtCore.QRect(1160, 90, 451, 511))
        self.widget_129.setStyleSheet("border-radius: 30px; /* Ajusta el valor para el radio de los bordes */\n"
"background-color:black;\n"
"border: none;            /* Borde negro */\n"
"border-radius: 20px;")
        self.widget_129.setObjectName("widget_129")
        self.label_439 = QtWidgets.QLabel(self.widget_129)
        self.label_439.setGeometry(QtCore.QRect(30, 20, 391, 461))
        self.label_439.setStyleSheet("border: none;")
        self.label_439.setText("")
        self.label_439.setPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/mano.png"))
        self.label_439.setScaledContents(True)
        self.label_439.setObjectName("label_439")
        self.label_440 = QtWidgets.QLabel(self.widget_25)
        self.label_440.setGeometry(QtCore.QRect(20, 60, 1091, 641))
        self.label_440.setStyleSheet("border: none;")
        self.label_440.setText("")
        self.label_440.setPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/columna.jpeg"))
        self.label_440.setScaledContents(True)
        self.label_440.setObjectName("label_440")
        self.widget_130 = QtWidgets.QWidget(self.widget_25)
        self.widget_130.setGeometry(QtCore.QRect(0, 0, 821, 61))
        self.widget_130.setStyleSheet("border-radius: 30px; /* Ajusta el valor para el radio de los bordes */\n"
"background-color:qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #E2E0E0, stop:1 #d2d2d2);\n"
"border: none;            /* Borde negro */\n"
"border-radius: none;")
        self.widget_130.setObjectName("widget_130")
        self.pushButton_231 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_231.setGeometry(QtCore.QRect(0, 0, 81, 61))
        self.pushButton_231.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_231.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/iconcarpeta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_231.setIcon(icon9)
        self.pushButton_231.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_231.setObjectName("pushButton_231")
        self.pushButton_232 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_232.setGeometry(QtCore.QRect(80, 0, 81, 61))
        self.pushButton_232.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_232.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/iconsave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_232.setIcon(icon10)
        self.pushButton_232.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_232.setObjectName("pushButton_232")
        self.pushButton_233 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_233.setGeometry(QtCore.QRect(160, 0, 81, 61))
        self.pushButton_233.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_233.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/iconherra1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_233.setIcon(icon11)
        self.pushButton_233.setIconSize(QtCore.QSize(80, 70))
        self.pushButton_233.setObjectName("pushButton_233")
        self.pushButton_234 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_234.setGeometry(QtCore.QRect(240, 0, 81, 61))
        self.pushButton_234.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_234.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/fecha_atrasg-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_234.setIcon(icon12)
        self.pushButton_234.setIconSize(QtCore.QSize(40, 70))
        self.pushButton_234.setObjectName("pushButton_234")
        self.pushButton_235 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_235.setGeometry(QtCore.QRect(320, 0, 81, 61))
        self.pushButton_235.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_235.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/fecha_adelanteg-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_235.setIcon(icon13)
        self.pushButton_235.setIconSize(QtCore.QSize(40, 70))
        self.pushButton_235.setObjectName("pushButton_235")
        self.pushButton_236 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_236.setGeometry(QtCore.QRect(400, 0, 81, 61))
        self.pushButton_236.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_236.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/3d-icon-9783.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_236.setIcon(icon14)
        self.pushButton_236.setIconSize(QtCore.QSize(50, 70))
        self.pushButton_236.setObjectName("pushButton_236")
        self.pushButton_237 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_237.setGeometry(QtCore.QRect(480, 0, 81, 61))
        self.pushButton_237.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_237.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/icon2d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_237.setIcon(icon15)
        self.pushButton_237.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_237.setObjectName("pushButton_237")
        self.pushButton_238 = QtWidgets.QPushButton(self.widget_130)
        self.pushButton_238.setGeometry(QtCore.QRect(560, 0, 81, 61))
        self.pushButton_238.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_238.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/reproductor-de-videog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_238.setIcon(icon16)
        self.pushButton_238.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_238.setObjectName("pushButton_238")
        self.desplegablebotoncarpeta = QtWidgets.QWidget(self.widget_25)
        self.desplegablebotoncarpeta.setGeometry(QtCore.QRect(0, 60, 211, 61))
        self.desplegablebotoncarpeta.setStyleSheet("background-color:qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #E2E0E0, stop:1 #d2d2d2);\n"
"border: 1px solid #A0A0A0;\n"
"border-radius: 0px;\n"
"")
        self.desplegablebotoncarpeta.setObjectName("desplegablebotoncarpeta")
        self.pushButton_45 = QtWidgets.QPushButton(self.desplegablebotoncarpeta)
        self.pushButton_45.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.pushButton_45.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_56 = QtWidgets.QPushButton(self.desplegablebotoncarpeta)
        self.pushButton_56.setGeometry(QtCore.QRect(0, 30, 211, 31))
        self.pushButton_56.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_56.setObjectName("pushButton_56")
        self.desplegablebotonherramientas = QtWidgets.QWidget(self.widget_25)
        self.desplegablebotonherramientas.setGeometry(QtCore.QRect(160, 60, 211, 91))
        self.desplegablebotonherramientas.setStyleSheet("background-color:qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #E2E0E0, stop:1 #d2d2d2);\n"
"border: 1px solid #A0A0A0;\n"
"border-radius: 0px;\n"
"")
        self.desplegablebotonherramientas.setObjectName("desplegablebotonherramientas")
        self.pushButton_57 = QtWidgets.QPushButton(self.desplegablebotonherramientas)
        self.pushButton_57.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.pushButton_57.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.desplegablebotonherramientas)
        self.pushButton_58.setGeometry(QtCore.QRect(0, 30, 211, 31))
        self.pushButton_58.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.desplegablebotonherramientas)
        self.pushButton_59.setGeometry(QtCore.QRect(0, 60, 211, 31))
        self.pushButton_59.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_59.setObjectName("pushButton_59")
        self.desplegableboton2d = QtWidgets.QWidget(self.widget_25)
        self.desplegableboton2d.setGeometry(QtCore.QRect(480, 60, 211, 91))
        self.desplegableboton2d.setStyleSheet("background-color:qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #E2E0E0, stop:1 #d2d2d2);\n"
"border: 1px solid #A0A0A0;\n"
"border-radius: 0px;\n"
"")
        self.desplegableboton2d.setObjectName("desplegableboton2d")
        self.pushButton_60 = QtWidgets.QPushButton(self.desplegableboton2d)
        self.pushButton_60.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.pushButton_60.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.desplegableboton2d)
        self.pushButton_61.setGeometry(QtCore.QRect(0, 30, 211, 31))
        self.pushButton_61.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.desplegableboton2d)
        self.pushButton_62.setGeometry(QtCore.QRect(0, 60, 211, 31))
        self.pushButton_62.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_62.setObjectName("pushButton_62")
        self.widget_26 = QtWidgets.QWidget(self.widget_25)
        self.widget_26.setGeometry(QtCore.QRect(1010, 20, 611, 391))
        self.widget_26.setStyleSheet("border-radius: 30px; /* Ajusta el valor para el radio de los bordes */\n"
"background-color:#201F1F;\n"
"border: none;            /* Borde negro */\n"
"border-radius: 20px;")
        self.widget_26.setObjectName("widget_26")
        self.label_445 = QtWidgets.QLabel(self.widget_26)
        self.label_445.setGeometry(QtCore.QRect(30, 20, 501, 31))
        self.label_445.setStyleSheet("background: transparent;\n"
"border: none;")
        self.label_445.setObjectName("label_445")
        self.textEdit_24 = QtWidgets.QTextEdit(self.widget_26)
        self.textEdit_24.setGeometry(QtCore.QRect(30, 70, 551, 221))
        self.textEdit_24.setStyleSheet("background-color: #d3d3d3;   \n"
"padding: 10px;")
        self.textEdit_24.setObjectName("textEdit_24")
        self.label_446 = QtWidgets.QLabel(self.widget_26)
        self.label_446.setGeometry(QtCore.QRect(30, 310, 141, 51))
        self.label_446.setStyleSheet("background: transparent;\n"
"border: none;")
        self.label_446.setObjectName("label_446")
        self.pushButton_247 = QtWidgets.QPushButton(self.widget_26)
        self.pushButton_247.setGeometry(QtCore.QRect(450, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_247.setFont(font)
        self.pushButton_247.setMouseTracking(False)
        self.pushButton_247.setStyleSheet("QPushButton {\n"
"    background-color: #e92030;  /* Fondo transparente */\n"
"    border: none;              /* Borde blanco */\n"
"    border-radius: 18px;                  /* Bordes redondeados */\n"
"    color:  white;                         /* Color del texto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_247.setObjectName("pushButton_247")
        self.pushButton_248 = QtWidgets.QPushButton(self.widget_26)
        self.pushButton_248.setGeometry(QtCore.QRect(300, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_248.setFont(font)
        self.pushButton_248.setMouseTracking(False)
        self.pushButton_248.setStyleSheet("QPushButton {\n"
"    background-color: #2C872C;  /* Fondo transparente */\n"
"    border: none;              /* Borde blanco */\n"
"    border-radius: 18px;                  /* Bordes redondeados */\n"
"    color:  white;                         /* Color del texto */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 0.2);  /* Fondo ligeramente blanco al pasar el ratón */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 0.4);   /* Fondo más opaco al hacer clic */\n"
"}")
        self.pushButton_248.setObjectName("pushButton_248")
        self.checkBox = QtWidgets.QCheckBox(self.widget_26)
        self.checkBox.setGeometry(QtCore.QRect(110, 343, 21, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.Boton_Atras_71 = QtWidgets.QPushButton(self.widget_26)
        self.Boton_Atras_71.setGeometry(QtCore.QRect(560, 15, 41, 41))
        self.Boton_Atras_71.setStyleSheet("QPushButton {\n"
"    background-position: center;    /* Centrar la imagen */\n"
"    background-size: contain;\n"
"    background-color: transparent;    /* Cambiar el tamaño de la imagen (ajusta según sea necesario) */\n"
"    border: none;                   /* Elimina el borde del botón */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Color de fondo cuando el mouse está sobre el botón */\n"
"    color: white;               /* Color del texto al hacer hover */\n"
"    border: none;  /* Cambiar el color del borde al hacer hover */\n"
"}")
        self.Boton_Atras_71.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/EXIS.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Boton_Atras_71.setIcon(icon17)
        self.Boton_Atras_71.setIconSize(QtCore.QSize(20, 20))
        self.Boton_Atras_71.setObjectName("Boton_Atras_71")
        self.frameBotonesMenu_4 = QtWidgets.QFrame(self.ensayo)
        self.frameBotonesMenu_4.setGeometry(QtCore.QRect(20, 0, 151, 1021))
        self.frameBotonesMenu_4.setStyleSheet("background-color: rgb(101, 101, 101);")
        self.frameBotonesMenu_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBotonesMenu_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBotonesMenu_4.setObjectName("frameBotonesMenu_4")
        self.botonHome_4 = QtWidgets.QPushButton(self.frameBotonesMenu_4)
        self.botonHome_4.setGeometry(QtCore.QRect(10, 60, 131, 51))
        self.botonHome_4.setMinimumSize(QtCore.QSize(131, 0))
        self.botonHome_4.setStyleSheet("QPushButton {\n"
"    border: none;                   /* Elimina el borde del botón */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Color de fondo cuando el mouse está sobre el botón */\n"
"    color: white;               /* Color del texto al hacer hover */\n"
"    border: 1px solid #1c669b;  /* Cambiar el color del borde al hacer hover */\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonHome_4.setText("")
        self.botonHome_4.setIcon(icon2)
        self.botonHome_4.setIconSize(QtCore.QSize(50, 50))
        self.botonHome_4.setObjectName("botonHome_4")
        self.botonEdit_7 = QtWidgets.QPushButton(self.frameBotonesMenu_4)
        self.botonEdit_7.setGeometry(QtCore.QRect(10, 160, 131, 51))
        self.botonEdit_7.setMinimumSize(QtCore.QSize(131, 0))
        self.botonEdit_7.setStyleSheet("QPushButton {\n"
"    border: none;                   /* Elimina el borde del botón */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Color de fondo cuando el mouse está sobre el botón */\n"
"    color: white;               /* Color del texto al hacer hover */\n"
"    border: 1px solid #1c669b;  /* Cambiar el color del borde al hacer hover */\n"
"}")
        
        
        self.botonEdit_7.setText("")
        self.botonEdit_7.setIcon(icon3)

        self.botonEdit_7.setIconSize(QtCore.QSize(50, 50))
        self.botonEdit_7.setObjectName("botonEdit_7")
        self.botonUser_4 = QtWidgets.QPushButton(self.frameBotonesMenu_4)
        self.botonUser_4.setGeometry(QtCore.QRect(10, 860, 131, 51))
        self.botonUser_4.setMinimumSize(QtCore.QSize(131, 0))
        self.botonUser_4.setStyleSheet("QPushButton {\n"
"    border: none;                   /* Elimina el borde del botón */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Color de fondo cuando el mouse está sobre el botón */\n"
"    color: white;               /* Color del texto al hacer hover */\n"
"    border: 1px solid #1c669b;  /* Cambiar el color del borde al hacer hover */\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/6TO_SEMESTRE/Hologramas/icon/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonUser_4.setText("")
        self.botonUser_4.setIcon(icon4)
        self.botonUser_4.setIconSize(QtCore.QSize(70, 70))
        self.botonUser_4.setObjectName("botonUser_4")
        self.botonEdit_8 = QtWidgets.QPushButton(self.frameBotonesMenu_4)
        self.botonEdit_8.setGeometry(QtCore.QRect(240, 270, 131, 51))
        self.botonEdit_8.setMinimumSize(QtCore.QSize(131, 0))
        self.botonEdit_8.setStyleSheet("QPushButton {\n"
"    background-image: url(\"E:/6TO SEMESTRE/C:/6TO_SEMESTRE/Hologramas/icon/edit.png\"); /* Ruta de la imagen */\n"
"    background-position: center;    /* Centrar la imagen */\n"
"    background-repeat: no-repeat;   /* Evitar que se repita la imagen */\n"
"    background-size: contain;    /* Cambiar el tamaño de la imagen (ajusta según sea necesario) */\n"
"    border: none;                   /* Elimina el borde del botón */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Color de fondo cuando el mouse está sobre el botón */\n"
"    color: white;               /* Color del texto al hacer hover */\n"
"    border: 1px solid #1c669b;  /* Cambiar el color del borde al hacer hover */\n"
"}")
        self.botonEdit_8.setText("")
        self.botonEdit_8.setObjectName("botonEdit_8")
        self.cambianteTodo.addWidget(self.ensayo)
        self.cambianteTodo.addWidget(self.ensayo)
        fondoMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fondoMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1927, 26))
        self.menubar.setObjectName("menubar")
        fondoMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fondoMain)
        self.statusbar.setObjectName("statusbar")
        fondoMain.setStatusBar(self.statusbar)

        self.retranslateUi(fondoMain)
        self.cambianteTodo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(fondoMain)
        
   def retranslateUi(self, fondoMain):
        _translate = QtCore.QCoreApplication.translate
        fondoMain.setWindowTitle(_translate("fondoMain", "MainWindow"))
        self.label_433.setText(_translate("fondoMain", "<html><head/><body><p>Hola usuario1</p></body></html>"))
        self.label_434.setText(_translate("fondoMain", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#e6cab8;\">Estas en el ensayo del paciente</span></p></body></html>"))
        self.label_436.setText(_translate("fondoMain", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#e6cab8;\">Alejandro Javier Martinez</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#e6cab8;\">EXP213</span></p></body></html>"))
        self.pushButton_230.setText(_translate("fondoMain", "BACK"))
        self.label_437.setText(_translate("fondoMain", "<html><head/><body><p align=\"center\"><span style=\" color:#f00d11;\">ZOOM IN</span></p></body></html>"))
        self.label_438.setText(_translate("fondoMain", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#e6cab8;\">Tu acción:</span></p></body></html>"))
        self.pushButton_45.setText(_translate("fondoMain", "Open DICOM folder"))
        self.pushButton_56.setText(_translate("fondoMain", "Open DICOM file"))
        self.pushButton_57.setText(_translate("fondoMain", "Seleccionar"))
        self.pushButton_58.setText(_translate("fondoMain", "Cortar"))
        self.pushButton_59.setText(_translate("fondoMain", "Zoom"))
        self.pushButton_60.setText(_translate("fondoMain", "Vista 1"))
        self.pushButton_61.setText(_translate("fondoMain", "Vista 2"))
        self.pushButton_62.setText(_translate("fondoMain", "Vista 3"))
        self.label_445.setText(_translate("fondoMain", "<html><head/><body><p><span style=\" font-size:14pt; color:#e6cab8;\">Agregue las notas para este momento - Nota 01:</span></p></body></html>"))
        self.textEdit_24.setHtml(_translate("fondoMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#242525;\">En esta imagen se aprecia una fractura en la columna vertebral, donde una de las vértebras presenta una ruptura significativa. Esta lesión puede comprometer la estabilidad de la columna y, en algunos casos, afectar la médula espinal, lo que podría ocasionar problemas neurológicos.</span></p></body></html>"))
        self.label_446.setText(_translate("fondoMain", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#e6cab8;\">Agregar Imagen </span></p><p><span style=\" font-size:10pt; font-weight:600; color:#e6cab8;\">Actual:</span></p></body></html>"))
        self.pushButton_247.setText(_translate("fondoMain", "ACCEPT"))
        self.pushButton_248.setText(_translate("fondoMain", "REJECT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fondoMain = QtWidgets.QMainWindow()
    ui = Ui_fondoMain()
    ui.setupUi(fondoMain)
    fondoMain.show()
    #ui.setup_connections()
    sys.exit(app.exec_())  