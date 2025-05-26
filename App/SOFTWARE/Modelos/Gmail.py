import re
import os
import ssl
import smtplib
import random
import string
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

email_sender = "hospitalcarrionrecuperarcuenta@gmail.com"
password = os.getenv("PASSWORD")
codigo_enviado = ""

def generar_codigo_verificacion():
    caracteres = string.ascii_uppercase + string.digits
    codigo = ''.join(random.choice(caracteres) for i in range(5))
    return codigo

def enviar_codigo_verificacion(email_reciver):
    global codigo_enviado
    codigo_enviado = generar_codigo_verificacion()
    
    # Verificar si el correo está vacío o tiene formato incorrecto
    if not email_reciver or not re.match(r"[^@]+@[^@]+\.[^@]+", email_reciver):
        print("Error: Dirección de correo electrónico no válida.")
        return False

    subject = "Correo de verificación"
    body = f"Este es un correo de verificación de tu cuenta. \nTu código de recuperación es: {codigo_enviado}"

    em = EmailMessage()
    em["From"] = email_sender  # Asegúrate de que email_sender esté definido
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)  # Asegúrate de que password esté definido
            smtp.send_message(em)
            print("Correo enviado correctamente.")
            return True
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación. Verifica el correo y la contraseña.")
        return False
    except smtplib.SMTPException as e:
        print("Error al enviar el correo:", e)
        return False

def verificar_codigo(codigo_ingresado):
    if codigo_ingresado == codigo_enviado:
        return True
    else:
        return False