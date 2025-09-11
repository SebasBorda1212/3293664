import random

def batalla(p):
    if not p:
        print("Primero debes crear un personaje.")
        return

    enemigo_vida = 50
    print(f"\n{p['nombre']} entra en batalla contra un Orco")

    while p["vida"] > 0 and enemigo_vida > 0:
        enemigo_vida -= random.randint(5, p["ataque"])
        p["vida"] -= random.randint(3, 10)

    if p["vida"] > 0:
        print("Ganaste la batalla.")
    else:
        print("Has sido derrotado.")
