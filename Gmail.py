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
    
    subject = "Correo de verificación"
    body = f"Este es un correo de verificación de tu cuenta. \nTu código de recuperación es: {codigo_enviado}"
    
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.send_message(em)
    except Exception as e:
        print(f"Ocurrió un error al enviar el correo: {e}")

def verificar_codigo(codigo_ingresado):
    if codigo_ingresado == codigo_enviado:
        return True
    else:
        return False