# Ejercicio 27 : Búsqueda lineal
def buscar(lista, valor):
    for i, v in enumerate(lista):
        if v == valor:
            return i
    return -1
print(buscar([10,20,30,40], 30))
