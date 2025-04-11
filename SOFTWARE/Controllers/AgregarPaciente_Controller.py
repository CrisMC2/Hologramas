from PyQt5 import QtCore, QtGui, QtWidgets
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
    
def validar_direccion(texto, widget_padre, label_name, clase_instancia, distancia, parametro):
    eliminar_label_existente(clase_instancia, label_name)
    
    # Acepta letras, números, espacios, puntos, comas, guiones, numeral y acentos
    patron = r"^[\w\s\.\#\-\u00C0-\u017F\,]+$"
    
    if not re.match(patron, texto):
        label = añadir_label(widget_padre, f"{parametro} incorrecto ingresado", 130, distancia, 351, 31, label_name)
        setattr(clase_instancia, label_name, label)
        print(f"{parametro} incorrecto ingresado")
        return False
    else:
        print(f"{parametro} correcto ingresado")
        return True

def mostrar_calendario(ui, event):
    ui.calendar.show()
    QtWidgets.QTextEdit.mousePressEvent(ui.textEdit_18, event)

def colocar_fecha(ui, date):
    fecha = date.toString("dd/MM/yyyy")  
    ui.textEdit_18.setText(fecha)
    ui.calendar.hide()


def abrir_imagen(self, event):
    opciones = QFileDialog.Options()
    archivo, _ = QFileDialog.getOpenFileName(
        None, "Seleccionar Imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp)", options=opciones
    )
    
    if archivo:
        pixmap = QPixmap(archivo)
        pixmap = pixmap.scaled(self.label_157.width(), self.label_157.height(), aspectRatioMode=1)
        self.label_157.setPixmap(pixmap)
        
        # Guardar la ruta del archivo para su uso posterior
        self.foto_path = archivo

def subir_radiografia(self, event):
    # Inicializa la lista si no existe aún
    if not hasattr(self, 'radiografias_paths'):
        self.radiografias_paths = []

    rutas_archivos, _ = QFileDialog.getOpenFileNames(
        parent=None,
        caption="Seleccionar radiografías DICOM",
        directory="",
        filter="Archivos DICOM (*.dcm)"
    )

    if rutas_archivos:
        print(f"Radiografías seleccionadas: {rutas_archivos}")

        self.radiografias_paths.extend(rutas_archivos)
        self.radiografias_paths = list(set(self.radiografias_paths))  # eliminar duplicados

        rutas_texto = '\n'.join(self.radiografias_paths)
        self.textEdit_17.setText(rutas_texto)

def obtener_proximo_id():
    conn = conectar()
    cursor = conn.cursor()
    
    # Obtener el ID más alto actual
    cursor.execute("SELECT MAX(id_paciente) FROM PACIENTES")
    resultado = cursor.fetchone()
    
    # Si no hay pacientes, el ID comienza desde 1
    if resultado[0] is None:
        proximo_id = 1
    else:
        proximo_id = resultado[0] + 1
    
    conn.close()
    return proximo_id

def action_button2(self, button_id):
        if button_id == 14:
                # Obtener el próximo ID de paciente
                proximo_id = obtener_proximo_id()
                
                # Mostrar el próximo ID en el label_35 con el formato deseado
                self.label_35.setText(f"NEW EXP - N° {proximo_id}")
                # Cambiar el color del texto a blanco
                self.label_35.setStyleSheet("color: #e6cab8")

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
            # Obtener el próximo ID de paciente antes de la validación
            proximo_id = obtener_proximo_id()

            campos = {
                'nombre': (self.textEdit_20.toPlainText().strip(), self.widget_34, 'label_nombre', 47),
                'apellido': (self.textEdit_19.toPlainText().strip(), self.widget_33, 'label_apellido', 50),
                'domicilio': (self.textEdit_14.toPlainText().strip(), self.widget_29, 'label_domicilio', 50),
                'dni': (self.textEdit_21.toPlainText().strip(), self.widget_35, 'label_dni', 50),
                'correo': (self.textEdit_16.toPlainText().strip(), self.widget_31, 'label_correo', 50),
                'fecha': (self.textEdit_18.toPlainText().strip(), self.widget_32, 'label_fecha', 50),
                'telefono': (self.textEdit_15.toPlainText().strip(), self.widget_30, 'label_telefono', 50),
            }

            # Variables de validación
            nombre_valido = apellido_valido = domicilio_valido = dni_valido = correo_valido = fecha_valida = telefono_valido = False
            campos_vacios = False

            # Validación de los campos
            for key, (valor, widget, label_name, distancia) in campos.items():
                eliminar_label_existente(self, label_name)

                if not valor:
                    label = añadir_label(widget, f"{key.capitalize()} no puede estar vacío", 130, distancia, 351, 31, label_name)
                    setattr(self, label_name, label)
                    campos_vacios = True
                    continue  

                if key == 'nombre':
                    nombre_valido = validar_solo_letras(valor, widget, label_name, self, distancia, "Nombre")
                elif key == 'apellido':
                    apellido_valido = validar_solo_letras(valor, widget, label_name, self, distancia, "Apellido")
                elif key == 'domicilio':
                    domicilio_valido = validar_direccion(valor, widget, label_name, self, distancia, "Domicilio")
                elif key == 'dni':
                    dni_valido = valor.isdigit() and len(valor) == 8
                    if not dni_valido:
                        label = añadir_label(widget, "DNI incorrecto", 130, distancia, 351, 31, label_name)
                        setattr(self, label_name, label)
                elif key == 'correo':
                    correo_valido = validar_correo(self, valor, widget, label_name, distancia)
                elif key == 'fecha':
                    fecha_valida = validar_fecha(self, valor, widget, label_name, distancia)
                elif key == 'telefono':
                    telefono_valido = valor.isdigit() and len(valor) == 9
                    if not telefono_valido:
                        label = añadir_label(widget, "Teléfono incorrecto", 130, distancia, 351, 31, label_name)
                        setattr(self, label_name, label)

            # Si algún campo está vacío, se detiene el proceso
            if campos_vacios:
                print("Al menos un campo está vacío")
                return

            # Si todos los campos son válidos
            if all([nombre_valido, apellido_valido, domicilio_valido, dni_valido, correo_valido, fecha_valida, telefono_valido]):
                print("Todos los datos ingresados son válidos")

                # Obtener los datos para guardar en la base de datos
                apellidos = self.textEdit_19.toPlainText().strip()
                nombre = self.textEdit_20.toPlainText().strip()
                fecha_creacion = datetime.now().strftime("%Y-%m-%d")  # Fecha actual
                domicilio = self.textEdit_14.toPlainText().strip()
                telefono = self.textEdit_15.toPlainText().strip()
                email = self.textEdit_16.toPlainText().strip()
                identificacion = self.textEdit_21.toPlainText().strip()

                foto_path = self.foto_path  # Obtener la ruta en lugar de llamar a .pixmap()
                radiografia_path = self.textEdit_17.toPlainText().strip()  # Obtener la radiografía desde el QTextEdit
                radiografias_paths = self.radiografias_paths

                if not foto_path or not radiografias_paths:
                    print("Foto o radiografías no seleccionadas")
                    return

                # Guardar en la base de datos
                for radiografia_path in radiografias_paths:
                    agregar_paciente(
                        apellidos, nombre, fecha_creacion,
                        domicilio, telefono, email, identificacion,
                        foto_path, radiografia_path
                    )

                print(f"Paciente {nombre} {apellidos} agregado correctamente.")

                # Limpiar los campos después de agregar el paciente
                self.textEdit_19.clear()  # Apellido
                self.textEdit_20.clear()  # Nombre
                self.textEdit_14.clear()  # Domicilio
                self.textEdit_15.clear()  # Teléfono
                self.textEdit_16.clear()  # Email
                self.textEdit_21.clear()  # DNI
                self.textEdit_18.clear()  # Fecha
                self.textEdit_17.clear()  # Radiografía

                # También limpia la variable de la foto
                self.foto_path = ""
                self.label_157.setPixmap(QtGui.QPixmap()) 
