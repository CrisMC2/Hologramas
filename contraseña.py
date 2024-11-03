import bcrypt
import os

class User:
    def __init__(self):
        self.password_hash = None
        self.password_salt = None
        self.encrypted_password = None

    def set_password(self, password):
        self.set_password_salt()
        self.set_password_hash(password)
        self.set_password_encrypted()

    def set_password_salt(self):
        # Generar una sal aleatoria de 16 bytes
        self.password_salt = bcrypt.gensalt()

    def set_password_hash(self, password):
        # Hash de la contraseña utilizando la sal
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), self.password_salt)

    def set_password_encrypted(self):
        # Encriptar la contraseña hash para almacenamiento (opcional, dependiendo de tu diseño)
        self.encrypted_password = self.password_hash  # En este caso, solo almacenamos el hash

# Uso del código
user = User()
user.set_password("mi_contraseña_segura")
print("Hash de la contraseña:", user.password_hash)
print("Sal de la contraseña:", user.password_salt)