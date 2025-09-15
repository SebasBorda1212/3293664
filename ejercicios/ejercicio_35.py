# Ejercicio 35 : Compresión por conteo
texto = "aaabbc"
comprimido = ""
contador = 1
for i in range(1, len(texto)):
    if texto[i] == texto[i-1]:
        contador += 1
    else:
        comprimido += str(contador) + texto[i-1]
        contador = 1
comprimido += str(contador) + texto[-1]
print(comprimido)
