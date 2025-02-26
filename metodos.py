from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QListWidget, QVBoxLayout, QWidget, QMessageBox, QLineEdit, QListWidgetItem
from Gmail import enviar_codigo_verificacion, verificar_codigo
from PyQt5.QtCore import QTimer
from conexion import *
from conexion import obtener_guardados
from PyQt5.QtCore import Qt

def setup_connections(self):
        """Conecta las señales y eventos a los métodos correspondientes."""
        # Conectar el evento de clic en el campo de correo con el método que muestra la lista
        self.textEdit.mousePressEvent = self.showListWidget

        # Conectar el clic en un elemento de la lista con el método que gestiona la selección
        self.listWidget.itemClicked.connect(self.onItemClicked)

        # Conectar el botón de inicio de sesión con el método que gestiona la lógica de inicio de sesión
        #self.pushButton_11.clicked.connect(self.login)

def showListWidget(self, event):
        """Muestra el listWidget flotante cerca del campo de texto."""
        print("showListWidget ejecutado")  # Mensaje para depuración
        self.listWidget.clear()  # Limpiar el contenido actual del listWidget

        # Obtener los correos guardados solo cuando se necesiten
        self.saved_emails = obtener_guardados()  # Llamar a la función para obtener los correos guardados
        print(f"Correos guardados cargados: {self.saved_emails}")  # Para depuración
        # Verificar si hay correos guardados para mostrar
        if self.saved_emails:
                self.listWidget.addItems(self.saved_emails)  # Añadir los correos a la lista

        # Calcular la posición para que el listWidget aparezca justo debajo del campo de correo
        pos = self.textEdit.mapToGlobal(self.textEdit.rect().bottomLeft())
        self.listWidget.move(pos)  # Mover el listWidget a la posición calculada
        self.listWidget.show()  # Mostrar el listWidget

def onItemClicked(self, item):
        """Establece el correo seleccionado en el campo de texto."""
        print("Texto seleccionado:", item.text())  # Imprimir el correo seleccionado (depuración)
        self.textEdit.setText(item.text())  # Establecer el correo seleccionado en el campo de texto
        self.listWidget.hide()  # Ocultar el listWidget después de seleccionar un correo

def hideListWidget(self):
        print("Ocultando listWidget")  # Depuración: Verificar cuando se oculta el listWidget
        self.listWidget.hide()


def autoFocusNext(self, currentTextEdit, nextTextEdit):
        if len(currentTextEdit.toPlainText()) >= 1:
                nextTextEdit.setFocus()

def mask_password(self, textEdit, real_text_attr):
        textEdit.blockSignals(True)
        current_text = textEdit.toPlainText()
        real_text = getattr(self, real_text_attr)
        if len(current_text) < len(real_text):
                real_text = real_text[:len(current_text)]
        else:
                real_text += current_text[len(real_text):]
        setattr(self, real_text_attr, real_text)
        textEdit.setPlainText("*" * len(real_text))
        cursor = textEdit.textCursor()
        cursor.movePosition(cursor.End)
        textEdit.setTextCursor(cursor)
        textEdit.blockSignals(False)

def validateTextInput(self, textEdit, n):
        textEdit.blockSignals(True)
        text = textEdit.toPlainText()
        if len(text) > n:
                text = text[:n]
        text = text.replace(" ", "").replace("\n", "").replace("\t", "")
        textEdit.setPlainText(text)
        cursor = textEdit.textCursor()
        cursor.movePosition(cursor.End)
        textEdit.setTextCursor(cursor)
        textEdit.blockSignals(False)

def validateTextInput_2(self, textEdit, n):
        textEdit.blockSignals(True)
        text = textEdit.toPlainText()
        if len(text) > n:
                text = text[:n]
        text = text.replace("\n", "").replace("\t", "")
        textEdit.setPlainText(text)
        cursor = textEdit.textCursor()
        cursor.movePosition(cursor.End)
        textEdit.setTextCursor(cursor)
        textEdit.blockSignals(False)

def updateTextEditStyle(self, textEdit):
        if not textEdit.toPlainText:
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

#def onMousePressOutside(self, event):
    # Comprobar si el clic es fuera del QTextEdit y del QListWidget
    #if self.listWidget.isVisible():
            #if not (self.listWidget.geometry().contains(event.pos()) or self.textEdit.geometry().contains(event.pos())):
                    #self.listWidget.hide()
    #event.accept()