from Gmail import enviar_codigo_verificacion, verificar_codigo

email = "cristhianmartinezcasas@gmail.com"
enviar_codigo_verificacion(email)

codigo_usuario = input("Ingrese el código de verificación enviado: ")

if verificar_codigo(codigo_usuario):
    print("Verificación exitosa.")
else:
    print("Verificación fallida. Intente nuevamente.")