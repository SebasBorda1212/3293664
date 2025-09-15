# Ejercicio 7 : Descuento en cine
precio = 40
cantidad = 4
total = precio * cantidad
if cantidad >= 3:
    descuento = total * 0.15
    total -= descuento
    print("Descuento del 15% aplicado")
print("Total a pagar:", total)
