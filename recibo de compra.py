productos = ["arroz", "pasta", "sal", "huevos", "aceite"]
precios = [2000, 3000, 2500, 15000, 30000] 


comprador = input("Ingrese el nombre del comprador: ")

print("\n--- Lista de productos disponibles ---")
for indice, producto in enumerate(productos):
    print(indice, producto, "precio:", precios[indice])


seleccion = input("\nIngrese los números de los productos que va a comprar separados por comas: ")


seleccion = [int(x) for x in seleccion.split(",")]

print("\n--- Factura de compra ---")
print("Comprador:", comprador, "\n")

total_compra = 0
for indice in seleccion:
    producto = productos[indice]
    precio = precios[indice]
    iva = precio * 0.19
    total = precio + iva
    total_compra += total
    print(producto, precio, "→ con IVA:", int(total))

print("\nTOTAL de la compra con IVA:", int(total_compra))