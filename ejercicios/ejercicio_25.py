# Ejercicio 25 : Registro de productos
productos = []
def agregar_producto(nombre, precio):
    productos.append({"nombre": nombre, "precio": precio})
agregar_producto("Laptop", 1500)
agregar_producto("Mouse", 25)
print(productos)
