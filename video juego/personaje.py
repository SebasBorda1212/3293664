import random

def crear_personaje():
    nombre = input("Nombre: ")
    clase = input("Clase (Guerrero/Mago/Arquero): ")
    return {"nombre": nombre, "clase": clase, "vida": 100, "ataque": random.randint(8, 15)}

def ver_personaje(p):
    if p:
        print("\n=== PERSONAJE ===")
        print("Nombre:", p["nombre"])
        print("Clase:", p["clase"])
        print("Vida:", p["vida"])
        print("Ataque:", p["ataque"])
    else:
        print("No hay personaje creado.")
