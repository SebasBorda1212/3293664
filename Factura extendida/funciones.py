def mostrar_productos(productos, precios):
    print("\n--- Lista de productos disponibles ---")
    for indice, producto in enumerate(productos):
        print(indice, producto, "precio:", precios[indice])

def seleccionar_productos():
    seleccion = input("\nIngrese los números de los productos que va a comprar separados por comas: ")
    return [int(x) for x in seleccion.split(",")]
