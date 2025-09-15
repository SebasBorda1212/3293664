# Ejercicio 23 : Analizador de texto
def contar_vocales(texto):
    return sum(1 for c in texto.lower() if c in "aeiou")
print("Vocales en 'Programación':", contar_vocales("Programación"))
