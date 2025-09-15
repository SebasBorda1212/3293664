# Ejercicio 15 : Adivinar contraseña con intentos
password = "python123"
intentos = ["java123", "python", "python123"]
for intento in intentos:
    if intento == password:
        print("Contraseña correcta:", intento)
        break
    else:
        print("Intento fallido:", intento)
