import mysql.connector

tabla_medicos = "MEDICOS"
tabla_pacientes = "PACIENTES"

def conectar(sin_db=False):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Hospital_Carrion_Software" if not sin_db else None
    )

def crear_base_de_datos():
    conn = conectar(sin_db=True)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Hospital_Carrion_Software")
    conn.close()

def crear_tabla_medicos():
    conn = conectar()
    cursor = conn.cursor()
    crear_tabla_sql = """
    CREATE TABLE IF NOT EXISTS MEDICOS (
        id_medico INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        contraseña VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        description TEXT DEFAULT 'No hay descripción previa'
    )
    """
    cursor.execute(crear_tabla_sql)
    conn.close()

def crear_tabla_pacientes():
    conn = conectar()
    cursor = conn.cursor()
    crear_tabla_sql = """
    CREATE TABLE IF NOT EXISTS PACIENTES (
        id_paciente INT AUTO_INCREMENT PRIMARY KEY,
        apellidos VARCHAR(100) NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        fecha_creacion DATE,
        domicilio VARCHAR(100) NOT NULL,
        telefono VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        identificacion VARCHAR(20) NOT NULL UNIQUE,
        foto LONGBLOB,
        radiografia LONGBLOB
    )
    """
    cursor.execute(crear_tabla_sql)
    conn.close()
    
def crear_tabla_guardados():
    conn = conectar()
    cursor = conn.cursor()
    crear_tabla_sql = """
    CREATE TABLE IF NOT EXISTS GUARDADOS (
        email VARCHAR(100) NOT NULL UNIQUE
    )
    """
    cursor.execute(crear_tabla_sql)
    conn.close()

def eliminar_tabla_medicos():
    conn = conectar()
    cursor = conn.cursor()
    eliminar_tabla_sql = "DROP TABLE IF EXISTS MEDICOS"
    cursor.execute(eliminar_tabla_sql)
    conn.close()

def eliminar_tabla_pacientes():
    conn = conectar()
    cursor = conn.cursor()
    eliminar_tabla_sql = "DROP TABLE IF EXISTS PACIENTES"
    cursor.execute(eliminar_tabla_sql)
    conn.close()

def eliminar_tabla_guardados():
    conn = conectar()
    cursor = conn.cursor()
    eliminar_tabla_sql = "DROP TABLE IF EXISTS GUARDADOS"
    cursor.execute(eliminar_tabla_sql)
    conn.close()



def consulta_correo(correo):
    conn = conectar()
    cursor = conn.cursor()
    consulta_sql = f"SELECT COUNT(*) FROM {tabla_medicos} WHERE email = %s"
    cursor.execute(consulta_sql, (correo,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] > 0

def consulta_acceso_usuario(correo, contraseña):
    conn = conectar()
    cursor = conn.cursor()
    consulta_sql = f"SELECT COUNT(*) FROM {tabla_medicos} WHERE email = %s AND contraseña = %s"
    cursor.execute(consulta_sql, (correo, contraseña))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] > 0

def cambiar_contraseña(correo, nueva_contraseña):
    conn = conectar()
    cursor = conn.cursor()
    actualizar_sql = f"UPDATE MEDICOS SET contraseña = %s WHERE email = %s"
    cursor.execute(actualizar_sql, (nueva_contraseña, correo))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def agregar_medico(nombre, contraseña, email, description='No hay descripción previa'):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM MEDICOS WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    if resultado[0] > 0:
        print(f"El correo {email} ya está registrado. No se añadirá este médico.")
        conn.close()
        return
    agregar_sql = "INSERT INTO MEDICOS (nombre, contraseña, email, description) VALUES (%s, %s, %s, %s)"
    cursor.execute(agregar_sql, (nombre, contraseña, email, description))
    conn.commit()
    conn.close()
#d
def agregar_paciente(id_paciente, apellidos, nombre, fecha_creacion, domicilio, telefono, email, identificacion, foto_path, radiografia_path):
    conn = conectar()
    cursor = conn.cursor()
    
    # Verificar si ya existe un paciente con esa identificación
    cursor.execute("SELECT COUNT(*) FROM PACIENTES WHERE identificacion = %s", (identificacion,))
    resultado = cursor.fetchone()
    
    if resultado[0] > 0:
        print(f"El paciente con identificacion {identificacion} ya está registrado. No se añadirá este paciente.")
        conn.close()
        return
    
    # Leer imagen y radiografía en binario
    with open(foto_path, 'rb') as f:
        foto = f.read()
    with open(radiografia_path, 'rb') as f:
        radiografia = f.read()
    
    sql = """
        INSERT INTO PACIENTES 
        (id_paciente, apellidos, nombre, fecha_creacion, domicilio, telefono, email, identificacion, foto, radiografia)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    cursor.execute(sql, (
        id_paciente, apellidos, nombre, fecha_creacion, domicilio, telefono, email, identificacion, foto, radiografia
    ))
    
    conn.commit()
    conn.close()
    print(f"Paciente {nombre} {apellidos} agregado correctamente.")


def agregar_guardados(email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM GUARDADOS WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    if resultado[0] > 0:
        print(f"El correo {email} ya está registrado. No se añadirá este correo.")
        conn.close()
        return
    agregar_sql = "INSERT INTO GUARDADOS (email) VALUES (%s)"
    cursor.execute(agregar_sql, (email,))
    conn.commit()
    conn.close()

def iniciar():
    crear_tabla_medicos()
    crear_tabla_pacientes()
    crear_tabla_guardados()
    medicos = [
        ('Olenka', 'stivenss', 'olenkaanna23@gmail.com', 'Amarilla'),
        ('Cristhian', 'ingriddd', 'cristhianmartinezcasas@gmail.com', 'Yo')
    ]
    for medico in medicos:
        agregar_medico(*medico)
    global guardados
    guardados = [('olenkaanna23@gmail.com'),('cristhianmartinezcasas@gmail.com')]
    for guardado in guardados:
        agregar_guardados(guardado)

def obtener_guardados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT email
        FROM GUARDADOS 
    """)
    resultado = cursor.fetchall()  # Trae todos los resultados en una lista de tuplas
    emails = [fila[0] for fila in resultado] 
    conn.close()
    return emails  # Retorna la lista de tuplas (correo, contraseña)

def aumentar_max_packet():
    """Aumenta el tamaño máximo permitido para paquetes en MySQL."""
    conn = conectar(sin_db=True)  # Conectar sin base de datos para ejecutar la configuración global
    cursor = conn.cursor()
    cursor.execute("SET GLOBAL max_allowed_packet = 1073741824;")  # 1GB
    conn.commit()
    conn.close()
    print("✅ max_allowed_packet actualizado a 1GB")


def eliminar_todo():
    eliminar_tabla_medicos()
    eliminar_tabla_pacientes()
    eliminar_tabla_guardados()

# Aumentar max_allowed_packet antes de realizar operaciones grandes
aumentar_max_packet()

# Luego, ejecutar el resto del código
crear_base_de_datos()
iniciar()