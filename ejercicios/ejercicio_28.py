# Ejercicio 28 : Contador de letras
palabra = "banana"
frecuencia = {}
for letra in palabra:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1
print(frecuencia)
