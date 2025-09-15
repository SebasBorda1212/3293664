# Ejercicio 24 : Generador simple de contraseña
import random, string
def generar_password(longitud=6):
    return "".join(random.choice(string.ascii_letters) for _ in range(longitud))
print("Contraseña generada:", generar_password(10))
