# Ejercicio 31 : Simulación de batería
class Bateria:
    def __init__(self, carga=100):
        self.carga = carga
    def usar(self):
        self.carga -= 10
    def estado(self):
        return self.carga
b = Bateria()
b.usar()
print("Carga restante:", b.estado())
