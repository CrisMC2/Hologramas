from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QListWidget, QVBoxLayout, QWidget, QMessageBox, QLineEdit, QListWidgetItem
from Modelos.Gmail import enviar_codigo_verificacion, verificar_codigo
from PyQt5.QtCore import QTimer
from Modelos.conexion import *
from Modelos.conexion import obtener_guardados
from PyQt5.QtCore import Qt
import re
from datetime import datetime


def setup_connections(ui):
        """Conecta las señales y eventos a los métodos correspondientes."""
        ui.textEdit.mousePressEvent = lambda event: showListWidget(ui, event)
        ui.listWidget.itemClicked.connect(lambda item: onItemClicked(ui, item))
        

def showListWidget(ui, event):
        """Muestra el listWidget flotante cerca del campo de texto."""
        print("showListWidget ejecutado")  # Mensaje para depuración
        ui.listWidget.clear()  # Limpiar el contenido actual del listWidget
        ui.saved_emails = obtener_guardados()  # Obtener los correos guardados
        print(f"Correos guardados cargados: {ui.saved_emails}")  # Para depuración
        if ui.saved_emails:
                ui.listWidget.addItems(ui.saved_emails)  # Añadir los correos a la lista
        
        pos = ui.textEdit.mapToGlobal(ui.textEdit.rect().bottomLeft())
        ui.listWidget.move(pos)  # Mover el listWidget a la posición calculada
        ui.listWidget.show()  # Mostrar el listWidget

def onItemClicked(ui, item):
        """Establece el correo seleccionado en el campo de texto."""
        print("Texto seleccionado:", item.text())  # Para depuración
        ui.textEdit.setText(item.text())  # Establecer el correo seleccionado
        ui.listWidget.hide()  # Ocultar el listWidget después de seleccionar un correo

def autoFocusNext(self, currentTextEdit, nextTextEdit):
        if len(currentTextEdit.toPlainText()) >= 1:
                nextTextEdit.setFocus()

def mask_password(self, textEdit, real_text_attr):
        textEdit.blockSignals(True)  # Bloquear señales para evitar loops infinitos
        cursor = textEdit.textCursor()  # Guardar la posición actual del cursor
        position = cursor.position()  # Obtener la posición del cursor
        current_text = textEdit.toPlainText()
        real_text = getattr(self, real_text_attr, "")
        # Si el usuario eliminó caracteres
        if len(current_text) < len(real_text):
                real_text = real_text[:len(current_text)]
        # Si el usuario agregó caracteres en cualquier posición
        elif len(current_text) > len(real_text):
                difference = len(current_text) - len(real_text)
                real_text = real_text[:position - difference] + current_text[position - difference:position] + real_text[position - difference:]
        setattr(self, real_text_attr, real_text)
        textEdit.setPlainText("*" * len(real_text))  # Reemplazar el texto con asteriscos
        cursor.setPosition(position)  # Restaurar la posición del cursor
        textEdit.setTextCursor(cursor)
        textEdit.blockSignals(False)  # Reactivar señales

def validateTextInput(self, textEdit, n):
        textEdit.blockSignals(True)
        cursor = textEdit.textCursor()  # Guardar la posición del cursor
        position = cursor.position()
        text = textEdit.toPlainText()
        if len(text) > n:
                text = text[:n]
        text = text.replace(" ", "").replace("\n", "").replace("\t", "")
        textEdit.setPlainText(text)  # Establecer el texto sin espacios
        cursor.setPosition(position)  # Restaurar la posición del cursor
        textEdit.setTextCursor(cursor)
        textEdit.blockSignals(False)

def validateTextInput_2(self, textEdit, n):
        textEdit.blockSignals(True)  # Bloquea señales para evitar bucles infinitos
        cursor = textEdit.textCursor()  # Guarda la posición del cursor
        position = cursor.position()
        text = textEdit.toPlainText()
        if len(text) > n:
                text = text[:n]  # Limita la longitud del texto a 'n'
        textEdit.setPlainText(text)  # Aplica el texto corregido
        cursor.setPosition(position)  # Restaura la posición del cursor
        textEdit.setTextCursor(cursor)
        textEdit.blockSignals(False)  # Reactiva señales

def updateTextEditStyle(self, textEdit):
        if not textEdit.toPlainText():
                textEdit.setStyleSheet("""
                QTextEdit {
                color: #949494;
                border-top:none;
                border-right:none;
                border-left:none;
                border-bottom: 1px solid gray;
                font-size:14pt;
                }
                QTextEdit:placeholder {
                color: #949494;
                font-size:14pt;
                }
                """)
                placeholders = {
                self.textEdit: "Email user",
                self.textEdit_2: "Password",
                self.textEdit_3: "Ingresa tu email registrado",
                self.textEdit_4: "0",
                self.textEdit_5: "0",
                self.textEdit_6: "0",
                self.textEdit_7: "0",
                self.textEdit_8: "0",
                self.textEdit_9: "Ingresa una nueva contraseña",
                self.textEdit_10: "Confirma la contraseña",
                self.textEdit_11: "Ingresa tus apellidos y nombres",
                self.textEdit_12: "Ingresa tu correo electrónico",
                self.textEdit_13: "Crea una contraseña"
                }
                textEdit.setPlaceholderText(placeholders.get(textEdit, "0"))
        else:
                textEdit.setStyleSheet("""
                QTextEdit {
                color: white;
                border-top:none;
                border-right:none;
                border-left:none;
                border-bottom: 1px solid gray;
                font-size:14pt;
                }
                QTextEdit:placeholder {
                color: #949494;
                font-size:14pt;
                }
                """)
                textEdit.setPlaceholderText("")

def updateInputTextEdit(self, textEdit):
        if not textEdit.toPlainText():
                textEdit.setStyleSheet(""
                "QTextEdit {\n"
                "    border: 2px solid gray;        /* Bordes */\n"
                "    border-radius: 15px;           /* Esquinas redondeadas */\n"
                "    padding: 5px;                  /* Espacio interno para el texto */\n"
                "    background-color: #d3d3d3;       /* Color de fondo */\n"
                "    font-size: 14px;               /* Tamaño de fuente */\n"
                "    color: black;                  /* Color del texto */\n"
                "}\n"
                "\n"
                "QTextEdit:focus {\n"
                "    border-color:gray;            /* Cambia el color del borde al hacer foco */\n"
                "}")
                placeholders = {
                  self.textEdit_20 :"Ingrese los nombres del paciente",
                  self.textEdit_19 : "Ingrese los apellidos del paciente",
                  self.textEdit_14 : "Ingrese el domicilio del paciente",
                  self.textEdit_21 : "Ingrese la identificación del paciente",
                  self.textEdit_16 : "Ingrese el correo del paciente",
                  self.textEdit_18 : "dd/mm/yyyy - HH:mm",
                  self.textEdit_15 : "Ingrese el número de celular"
                }
                textEdit.setPlaceholderText(placeholders.get(textEdit, "0"))
        else:
                textEdit.setStyleSheet(""
                "QTextEdit {\n"
                "    border: 2px solid gray;        /* Bordes */\n"
                "    border-radius: 15px;           /* Esquinas redondeadas */\n"
                "    padding: 5px;                  /* Espacio interno para el texto */\n"
                "    background-color: #d3d3d3;       /* Color de fondo */\n"
                "    font-size: 14px;               /* Tamaño de fuente */\n"
                "    color: black;                  /* Color del texto */\n"
                "}\n"
                "\n"
                "QTextEdit:focus {\n"
                "    border-color:gray;            /* Cambia el color del borde al hacer foco */\n"
                "}")
                textEdit.setPlaceholderText("")

def eliminar_label_existente(clase_instancia, label_name):
    if hasattr(clase_instancia, label_name):
        getattr(clase_instancia, label_name).deleteLater()
        delattr(clase_instancia, label_name)

def añadir_label(widget_padre, texto, posicion_x, posicion_y, ancho, alto, nombre_label="label_generico", tamaño_fuente=7, color_texto="red"):
    label = QtWidgets.QLabel(widget_padre)
    label.setGeometry(QtCore.QRect(posicion_x, posicion_y, ancho, alto))

    font = QtGui.QFont()
    font.setPointSize(tamaño_fuente)
    label.setFont(font)

    label.setStyleSheet(f"QLabel {{ color: {color_texto}; background: none; }}")

    label.setText(texto)
    label.setObjectName(nombre_label)
    label.show()

    # Guardamos la referencia en la clase para poder eliminarlo luego
    return label

def validar_solo_letras(texto, widget_padre, label_name, clase_instancia, distancia, parametro):
    eliminar_label_existente(clase_instancia, label_name)

    if any(not (char.isalpha() or char.isspace()) for char in texto):
        label = añadir_label(widget_padre, f"{parametro} incorrecto ingresado", 130, distancia, 351, 31, label_name)
        setattr(clase_instancia, label_name, label)
        print(f"{parametro} incorrecto ingresado")
        return False
    else:
        print(f"{parametro} correcto ingresado")
        return True

def validar_correo(clase_instancia, texto, widget_padre, label_name, distancia):
    eliminar_label_existente(clase_instancia, label_name)
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'

    if re.match(patron, texto):
        print("Correo válido ingresado")
        return True
    else:
        label = añadir_label(widget_padre, "Correo incorrecto", 130, distancia, 351, 31, label_name)
        setattr(clase_instancia, label_name, label)
        print("Correo inválido ingresado")
        return False

def validar_fecha(clase_instancia, texto, widget_padre, label_name, distancia):
    eliminar_label_existente(clase_instancia, label_name)
    try:
        datetime.strptime(texto, "%d/%m/%Y")  # formato de fecha dd/mm/yyyy
        print("Fecha válida")
        return True
    except ValueError:
        label = añadir_label(widget_padre, "Fecha incorrecta", 130, distancia, 351, 31, label_name)
        setattr(clase_instancia, label_name, label)
        print("Fecha incorrecta")
        return False
def mostrar_calendario(ui, event):
    ui.calendar.show()
    QtWidgets.QTextEdit.mousePressEvent(ui.textEdit_18, event)

def colocar_fecha(ui, date):
    fecha = date.toString("dd/MM/yyyy")  
    ui.textEdit_18.setText(fecha)
    ui.calendar.hide()


def action_button(self, button_id):
        if button_id == 1:
                self.PaginasLogin.setCurrentWidget(self.pag02Login)
                self.Boton_Atras_10.show()
                self.Boton_Atras_12.hide()
        elif button_id == 2:
                self.PaginasLogin.setCurrentWidget(self.pag04Login)
                self.Boton_Atras_10.show()
                self.Boton_Atras_12.hide()
        elif button_id == 3:
                self.PaginasLogin.setCurrentWidget(self.pag01Login)
                self.textEdit.setText("")
                self.textEdit_2.setText("") 
                self.textEdit_3.setText("")
                self.textEdit_4.setText("")
                self.textEdit_5.setText("")
                self.textEdit_6.setText("")
                self.textEdit_7.setText("")
                self.textEdit_8.setText("")
                self.textEdit_11.setText("")
                self.textEdit_12.setText("")
                self.textEdit_13.setText("")
                self.textEdit_4.hide()
                self.textEdit_5.hide()
                self.textEdit_6.hide()
                self.textEdit_7.hide()
                self.textEdit_8.hide()
                self.label_5.hide()
                self.label_6.hide()
                self.label_10.hide()
                self.label_11.hide()
                self.label_12.hide()
                self.label_4.hide()
                self.pushButton_13.hide()
        elif button_id == 4:
                self.correo = self.textEdit.toPlainText()
                self.password = self.real_text
                if consulta_correo(self.correo):
                        self.label_13.hide()
                        if consulta_acceso_usuario(self.correo, self.password):
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Information)
                                msg.setWindowTitle("Bienvenido de nuevo")
                                msg.setText(f"Hola bienvenido de nuevo")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec_()
                                self.cambianteTodo.setCurrentWidget(self.home)
                                self.label_14.hide()
                                self.Boton_Atras_10.show()
                                self.Boton_Atras_12.hide()
                        else: 
                                self.label_14.show()
                else:
                        self.label_13.show()
        elif button_id == 5:
                user_text = self.textEdit_3.toPlainText()
                if consulta_correo(user_text):
                        enviar_codigo_verificacion(self.textEdit_3.toPlainText())
                        self.label_4.show()
                        self.label_6.show()
                        self.textEdit_4.show()
                        self.textEdit_5.show()
                        self.textEdit_6.show()
                        self.textEdit_7.show()
                        self.textEdit_8.show()
                        self.pushButton_13.show()
                        self.label_5.hide()
                else:
                        self.label_5.show()
        elif button_id == 6:
                code = self.textEdit_4.toPlainText() + self.textEdit_5.toPlainText() + self.textEdit_6.toPlainText() + self.textEdit_7.toPlainText() + self.textEdit_8.toPlainText()
                if verificar_codigo(code):
                        self.PaginasLogin.setCurrentWidget(self.pag03Login)
                        self.textEdit_4.setText("")
                        self.textEdit_5.setText("")
                        self.textEdit_6.setText("")
                        self.textEdit_7.setText("")
                        self.textEdit_8.setText("")
                        self.textEdit_4.hide()
                        self.textEdit_5.hide()
                        self.textEdit_6.hide()
                        self.textEdit_7.hide()
                        self.textEdit_8.hide()
                        self.label_4.hide()
                        self.label_6.hide()
                        self.textEdit_3.setText("")
                        self.label_5.hide()
                        self.pushButton_13.hide()
                else:
                        self.label_6.show()
                        self.textEdit_4.setText("")
                        self.textEdit_5.setText("")
                        self.textEdit_6.setText("")
                        self.textEdit_7.setText("")
                        self.textEdit_8.setText("")
        elif button_id == 7:
                if len(self.textEdit_9.toPlainText())>7:
                        self.label_8.hide()
                        if self.textEdit_9.toPlainText() == self.real_text_3:
                                cambiar_contraseña(self.correo, self.password)
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Information)
                                msg.setWindowTitle("Cambio de contraseña")
                                msg.setText("¡Contraseña cambiada exitosamente!")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec_()
                                self.cambianteTodo.setCurrentWidget(self.home)
                                self.textEdit_9.setText("")
                                self.textEdit_10.setText("")
                                self.label_25.hide()
                                self.Boton_Atras_26.show()
                                self.Boton_Atras_24.hide()
                        else:
                                self.label_25.show()
                else:
                        self.label_8.show()
        elif button_id == 8:
                if len(self.textEdit_11.toPlainText())>7:
                        self.label_10.hide()
                        if self.textEdit_12.toPlainText().count("@") == 1:
                                self.label_11.hide()
                                if len(self.real_text_4)>7:
                                        self.label_12.hide()
                                        self.user = self.textEdit_11.toPlainText()
                                        self.correo = self.textEdit_12.toPlainText()
                                        self.password = self.real_text_4
                                        if consulta_correo(self.correo):
                                                msg = QMessageBox()
                                                msg.setIcon(QMessageBox.Information)
                                                msg.setWindowTitle("Correo ya registrado")
                                                msg.setText(f"Lo siento. \nEl correo {self.correo} ya ha sido registrado por otro usuario.\nIntentelo de nuevo con otro correo.")
                                                msg.setStandardButtons(QMessageBox.Ok)
                                                msg.exec_()
                                                self.textEdit_12.setText("")
                                                self.label_11.show()
                                        else:
                                                if enviar_codigo_verificacion(self.correo):
                                                        self.PaginasLogin.setCurrentWidget(self.pag05Login)
                                                        self.textEdit_11.setText("")
                                                        self.textEdit_12.setText("")
                                                        self.textEdit_13.setText("")
                                                        self.label_12.hide()
                                                        self.Boton_Atras_69.show()
                                                        self.Boton_Atras_72.hide()
                                                else:
                                                        msg = QMessageBox()
                                                        msg.setIcon(QMessageBox.Information)
                                                        msg.setWindowTitle("Error de cuenta")
                                                        msg.setText(f"Lo siento. \nEl correo {self.correo} es inválido y no se pudo enviar el código de verificación.\nIntentelo de nuevo con otro correo.")
                                                        msg.setStandardButtons(QMessageBox.Ok)
                                                        msg.exec_()
                                                        self.textEdit_12.setText("")
                                                        self.label_11.show()
                                else:
                                        self.label_12.show()
                        else:
                                self.label_11.show()
                else:
                        self.label_10.show()
        elif button_id == 9:
                self.cambianteTodo.setCurrentWidget(self.home)
                self.PaginasHome.setCurrentWidget(self.pag_opciones)
        elif button_id == 10:
                code = self.textEdit_52.toPlainText() + self.textEdit_53.toPlainText() + self.textEdit_51.toPlainText() + self.textEdit_49.toPlainText() + self.textEdit_50.toPlainText()
                if verificar_codigo(code):
                        agregar_medico(self.user, self.password, self.correo)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Creación de cuenta")
                        msg.setText(f"¡Cuenta creada exitosamente!\nUsuario: {self.user}\nCorreo: {self.correo}")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                        self.label_386.hide()
                        self.textEdit_49.setText("")
                        self.textEdit_50.setText("")
                        self.textEdit_51.setText("")
                        self.textEdit_52.setText("")
                        self.textEdit_53.setText("")
                        self.cambianteTodo.setCurrentWidget(self.home)
                else:
                        self.label_386.show()
        elif button_id == 11:
                self.PaginasLogin.setCurrentWidget(self.pag04Login)
                self.label_386.hide()
                self.textEdit_49.setText("")
                self.textEdit_50.setText("")
                self.textEdit_51.setText("")
                self.textEdit_52.setText("")
                self.textEdit_53.setText("")
        elif button_id == 12:
                self.Boton_Atras_10.show()
                self.Boton_Atras_26.show()
                self.Boton_Atras_69.show()
                self.Boton_Atras_12.hide()
                self.Boton_Atras_24.hide()
                self.Boton_Atras_72.hide()
                self.real_text = self.textEdit_2.toPlainText()
                self.real_text_3 = self.textEdit_10.toPlainText()
                self.real_text_4 = self.textEdit_13.toPlainText()
                self.textEdit_2.textChanged.disconnect()
                self.textEdit_10.textChanged.disconnect()
                self.textEdit_13.textChanged.disconnect()
                self.textEdit_2.textChanged.connect(lambda: updateTextEditStyle(self, self.textEdit_2))
                self.textEdit_10.textChanged.connect(lambda: updateTextEditStyle(self, self.textEdit_10))
                self.textEdit_13.textChanged.connect(lambda: updateTextEditStyle(self, self.textEdit_13))
                self.textEdit_2.textChanged.connect(lambda: validateTextInput_2(self, self.textEdit_2, 42))
                self.textEdit_10.textChanged.connect(lambda: validateTextInput_2(self, self.textEdit_10, 42))
                self.textEdit_13.textChanged.connect(lambda: validateTextInput_2(self, self.textEdit_13, 42))
                self.textEdit_2.textChanged.connect(lambda: mask_password(self, self.textEdit_2, 'real_text'))
                self.textEdit_10.textChanged.connect(lambda: mask_password(self, self.textEdit_10, 'real_text_3'))
                self.textEdit_13.textChanged.connect(lambda: mask_password(self, self.textEdit_13, 'real_text_4'))
                self.textEdit_2.setText(self.real_text)
                self.textEdit_10.setText(self.real_text_3)
                self.textEdit_13.setText(self.real_text_4)
        elif button_id == 13:
                self.Boton_Atras_10.hide()
                self.Boton_Atras_26.hide()
                self.Boton_Atras_69.hide()
                self.Boton_Atras_12.show()
                self.Boton_Atras_24.show()
                self.Boton_Atras_72.show()
                self.textEdit_2.textChanged.disconnect()
                self.textEdit_10.textChanged.disconnect()
                self.textEdit_13.textChanged.disconnect()
                self.textEdit_2.textChanged.connect(lambda: updateTextEditStyle(self, self.textEdit_2))
                self.textEdit_10.textChanged.connect(lambda: updateTextEditStyle(self, self.textEdit_10))
                self.textEdit_13.textChanged.connect(lambda: updateTextEditStyle(self, self.textEdit_13))
                self.textEdit_2.textChanged.connect(lambda: validateTextInput_2(self, self.textEdit_2, 42))
                self.textEdit_10.textChanged.connect(lambda: validateTextInput_2(self, self.textEdit_10, 42))
                self.textEdit_13.textChanged.connect(lambda: validateTextInput_2(self, self.textEdit_13, 42))
                self.textEdit_2.setText(self.real_text)
                self.textEdit_10.setText(self.real_text_3)
                self.textEdit_13.setText(self.real_text_4)

        elif button_id == 14:
                self.cambianteTodo.setCurrentWidget(self.home)
                self.PaginasHome.setCurrentWidget(self.pag_agregar_paciente)
        
        elif button_id == 15:
                self.cambianteTodo.setCurrentWidget(self.home)
                self.PaginasHome.setCurrentWidget(self.pag_ver_paciente)
        
        elif button_id == 16:
                self.cambianteTodo.setCurrentWidget(self.home)
                self.PaginasHome.setCurrentWidget(self.pag_eliminar_paciente)
        elif button_id == 17:
                self.cambianteTodo.setCurrentWidget(self.home)
                self.PaginasHome.setCurrentWidget(self.pag_editar_paciente)
                self.Paginas_pag_editarpaciente.setCurrentWidget(self.Pag05_pageditarpaciente)
        elif button_id == 18:
                campos = {
                        'nombre': (self.textEdit_20.toPlainText().strip(), self.widget_34, 'label_nombre', 47),
                        'apellido': (self.textEdit_19.toPlainText().strip(), self.widget_33, 'label_apellido', 50),
                        'domicilio': (self.textEdit_14.toPlainText().strip(), self.widget_29, 'label_domicilio', 50),
                        'dni': (self.textEdit_21.toPlainText().strip(), self.widget_35, 'label_dni', 50),
                        'correo': (self.textEdit_16.toPlainText().strip(), self.widget_31, 'label_correo', 50),
                        'fecha': (self.textEdit_18.toPlainText().strip(), self.widget_32, 'label_fecha', 50),
                        'telefono': (self.textEdit_15.toPlainText().strip(), self.widget_30, 'label_telefono', 50),
                }

                #Variables para la validacion de datos
                nombre_valido = apellido_valido = domicilio_valido = dni_valido = correo_valido = fecha_valida = telefono_valido = False
                campos_vacios = False

                for key, (valor, widget, label_name, distancia) in campos.items():
                        # Siempre eliminar label anterior
                        eliminar_label_existente(self, label_name)

                        #Validar si está vacío
                        if not valor:
                                label = añadir_label(widget, f"{key.capitalize()} no puede estar vacío", 130, distancia, 351, 31, label_name)
                                setattr(self, label_name, label)
                                campos_vacios = True
                                continue  # No sigue validando formato si está vacío

                        #Validar formato específico según campo
                        if key == 'nombre':
                                nombre_valido = validar_solo_letras(valor, widget, label_name, self, distancia, "Nombre")

                        elif key == 'apellido':
                                apellido_valido = validar_solo_letras(valor, widget, label_name, self, distancia, "Apellido")

                        elif key == 'domicilio':
                                domicilio_valido = validar_solo_letras(valor, widget, label_name, self, distancia, "Domicilio")

                        elif key == 'dni':
                                if not (valor.isdigit() and len(valor) == 8):
                                        label = añadir_label(widget, "DNI incorrecto", 130, distancia, 351, 31, label_name)
                                        setattr(self, label_name, label)
                                        dni_valido = False
                                else:
                                        print("DNI correcto")
                                        dni_valido = True

                        elif key == 'correo':
                                correo_valido = validar_correo(self, valor, widget, label_name, distancia)

                        elif key == 'fecha':
                                fecha_valida = validar_fecha(self, valor, widget, label_name, distancia)

                        elif key == 'telefono':
                                if not (valor.isdigit() and len(valor) == 9):
                                        label = añadir_label(widget, "Teléfono incorrecto", 130, distancia, 351, 31, label_name)
                                        setattr(self, label_name, label)
                                        telefono_valido = False
                                else:
                                        print("Teléfono correcto")
                                        telefono_valido = True

                # Si hay algún campo vacío
                if campos_vacios:
                        print("Al menos un campo está vacío")
                        return

                # Si todos los datos han sido ingresados correctamente
                if all([nombre_valido, apellido_valido, domicilio_valido, dni_valido, correo_valido, fecha_valida, telefono_valido]):
                        print("Todos los datos ingresados son válidos")

                            
                          
                








#def onMousePressOutside(self, event):
# Comprobar si el clic es fuera del QTextEdit y del QListWidget
#if self.listWidget.isVisible():
        #if not (self.listWidget.geometry().contains(event.pos()) or self.textEdit.geometry().contains(event.pos())):
                #self.listWidget.hide()
#event.accept()

