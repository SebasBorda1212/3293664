# Ejercicio 26 : Ordenamiento de selección
def seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista
print(seleccion([5, 2, 9, 1]))
