from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QListWidget, QVBoxLayout, QWidget, QMessageBox, QLineEdit, QListWidgetItem
from Modelos.Gmail import enviar_codigo_verificacion, verificar_codigo
from PyQt5.QtCore import QTimer
from Modelos.conexion import *
from Modelos.conexion import obtener_guardados
from PyQt5.QtCore import Qt
import re
from datetime import datetime
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

pagina_actual = 1
paginas = 0

def actualizar_tabla(self, cambio):
    global pagina_actual, paginas
    paginas = numero_paginas()
    nueva_actualizacion = pagina_actual + cambio
    actualizar_botones(self, nueva_actualizacion, paginas)
    pagina_actual = nueva_actualizacion
    actualizar_tabla2(self)
    enfocar_pagina_actual(self)

def enfocar_pagina_actual(self):
    botones = [
        self.pushButton_20,
        self.pushButton_21,
        self.pushButton_22,
        self.pushButton_177
    ]
    style_default = (
        "QPushButton {"
        "    background-position: center;"
        "    background-repeat: no-repeat;"
        "    background-size: contain;"
        "    border: 2px solid #cccccc;"
        "    color: white;"
        "}"
        "QPushButton:hover {"
        "    background-color: #2980b9;"
        "    color: white;"
        "    border: 2px solid white;"
        "}"
    )
    style_activo = (
        "QPushButton {"
        "    background-color: #3498db;"  # Color más notorio
        "    background-position: center;"
        "    background-repeat: no-repeat;"
        "    background-size: contain;"
        "    border: 2px solid white;"
        "    color: white;"
        "}"
        "QPushButton:hover {"
        "    background-color: #1e94e3;"
        "    color: white;"
        "    border: 2px solid white;"
        "}"
    )
    for boton in botones:
        if int(boton.text()) == pagina_actual:
            boton.setStyleSheet(style_activo)
        else:
            boton.setStyleSheet(style_default)

def actualizar_tabla2(self):
    global pagina_actual
    lista_1 = [self.label_80, self.label_81, self.label_82, self.label_83, self.pushButton_19, self.widget_12]
    lista_2 = [self.label_84, self.label_85, self.label_86, self.label_104, self.pushButton_32, self.widget_13]
    lista_3 = [self.label_92, self.label_93, self.label_94, self.label_95, self.pushButton_37, self.widget_14]
    lista_4 = [self.label_96, self.label_97, self.label_98, self.label_99, self.pushButton_38, self.widget_15]
    lista_5 = [self.label_100, self.label_101, self.label_102, self.label_103, self.pushButton_39, self.widget_16]
    lista_general = [lista_1, lista_2, lista_3, lista_4, lista_5]
    pacientes = obtener_pacientes_resumen(pagina_actual - 1)
    for i in range(len(lista_general)):
        elementos = lista_general[i]
        if i < len(pacientes):
            paciente = pacientes[i]
            elementos[5].show()
            # Convertir foto (bytes) a QPixmap
            if paciente["foto"]:
                pixmap = QPixmap()
                pixmap.loadFromData(paciente["foto"])
                elementos[0].setPixmap(pixmap)
            else:
                pixmap = QPixmap("icon/foto_default.jpg")  # sin la barra al inicio si es relativa
                elementos[0].setPixmap(pixmap)
            # Mostrar ID y nombre completo (manteniendo su estilo)
            elementos[1].setText(f"EXP - N°{paciente['id']}")
            elementos[1].setStyleSheet("color: white; font-size: 12px;")
            elementos[1].setAlignment(Qt.AlignCenter)
            elementos[2].setText(f"{paciente['nombre']} {paciente['apellidos']}")
            elementos[2].setStyleSheet("color: white; font-size: 12px;")
            elementos[2].setAlignment(Qt.AlignCenter)
            elementos[3].setAlignment(Qt.AlignCenter)
            # Estado: radiografía disponible o no
            if paciente["radiografia"]:
                elementos[3].setText("Apto")
                # Solo cambia el color del texto para "Apto"
                elementos[3].setStyleSheet("color: green; font-size: 9pt;")
            else:
                elementos[3].setText("No apto")
                # Solo cambia el color del texto para "Faltan recursos"
                elementos[3].setStyleSheet("color: red; font-size: 9pt;")
            elementos[4].setEnabled(True)
        else:
            elementos[5].hide()
            
def actualizar_botones(self, nueva_actualizacion, paginas):
    # Mostrar por defecto
    self.pushButton_40.show()
    self.pushButton_23.show()
    self.label_47.show()
    # Ocultar botones según la cantidad de páginas
    if paginas == 1:
        for btn in [self.pushButton_21, self.pushButton_22, self.pushButton_177, self.pushButton_40, self.pushButton_23]:
            btn.hide()
        self.label_47.hide()
    elif paginas == 2:
        self.pushButton_22.hide()
        self.pushButton_177.hide()
        self.label_47.hide()
        if nueva_actualizacion == paginas:
            self.pushButton_23.hide()
        else:
            self.pushButton_40.hide()
    elif paginas == 3:
        self.pushButton_177.hide()
        if nueva_actualizacion == paginas:
            self.pushButton_23.hide()
        elif nueva_actualizacion == paginas - 2:
            self.pushButton_40.hide()
    else:
        if nueva_actualizacion == 1:
            self.pushButton_40.hide()
            numeros = [nueva_actualizacion + i for i in range(4)]
        elif nueva_actualizacion == paginas:
            self.pushButton_23.hide()
            numeros = [nueva_actualizacion - 3 + i for i in range(4)]
        elif nueva_actualizacion == paginas - 1:
            numeros = [nueva_actualizacion - 2 + i for i in range(4)]
        elif nueva_actualizacion <= paginas - 2:
            numeros = [nueva_actualizacion - 1 + i for i in range(4)]
        self.pushButton_20.setText(str(numeros[0]))
        self.pushButton_21.setText(str(numeros[1]))
        self.pushButton_22.setText(str(numeros[2]))
        self.pushButton_177.setText(str(numeros[3]))

def action_button4(self, button_id, pag_seleccionada):
    global pagina_actual
    if button_id == 1:
        actualizar_tabla(self, pag_seleccionada - pagina_actual)
    elif button_id == 2:
        actualizar_tabla(self, pag_seleccionada)