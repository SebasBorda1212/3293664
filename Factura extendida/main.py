
from productos import productos, precios
from funciones import mostrar_productos, seleccionar_productos
from factura import generar_factura


comprador = input("Ingrese el nombre del comprador: ")


mostrar_productos(productos, precios)


seleccion = seleccionar_productos()


generar_factura(comprador, seleccion, productos, precios)
