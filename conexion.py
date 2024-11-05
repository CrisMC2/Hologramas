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
        description TEXT
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

def cambiar_contraseña(tabla, correo, nueva_contraseña):
    conn = conectar()
    cursor = conn.cursor()
    actualizar_sql = f"UPDATE {tabla} SET contraseña = %s WHERE email = %s"
    cursor.execute(actualizar_sql, (nueva_contraseña, correo))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def agregar_medico(nombre, contraseña, email, description):
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

def iniciar():
    crear_tabla_medicos()
    crear_tabla_pacientes()
    medicos = [
        ('Olenka', 'stivenss', 'olenkaanna23@gmail.com', 'Amarilla'),
        ('Cristhian', 'ingriddd', 'cristhianmartinezcasas@gmail.com', 'Yo')
    ]
    for medico in medicos:
        agregar_medico(*medico)

def eliminar_todo():
    eliminar_tabla_medicos()
    eliminar_tabla_pacientes()

# Ejecutar la creación de la base de datos y las tablas
crear_base_de_datos()
iniciar()
