#Determinar si un número es positivo o negativo

numero = float(input("Ingrese un número: "))

if numero > 0:
    print("El número es POSITIVO.")
elif numero < 0:
    print("El número es NEGATIVO.")
else:
    print("El número es CERO.")