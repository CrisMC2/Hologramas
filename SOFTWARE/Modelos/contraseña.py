import bcrypt

def set_password(password):
    password_salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), password_salt)
    return password_hash

def check_password(stored_password_hash, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_password_hash)

password = "mi_contraseña_segura"
stored_password_hash = set_password(password)
print("Hash de la contraseña almacenado:", stored_password_hash)

input_password = "mi_contraseña_segura"
if check_password(stored_password_hash, input_password):
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")