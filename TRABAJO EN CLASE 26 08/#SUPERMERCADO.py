#SUPERMERCADO
nombre=input("ingrese el nombre del comprador")
fecha=input("ingrese la fecha de la compra dd/mm/aaaa/")
print("--------Factura de compra--------")
print("FECHA DE COMPRA:", fecha )
print("CLIENTE:", nombre  )    
productos=["arroz","pasta","sal","huevos","aceite"]
precios=[2000, 3000, 2500,15000, 30000]
print("PRODUCTOS DISPONIBLES")
for indice, listado in enumerate(productos):
    iva=precios[indice]* 0.19
    total=precios[indice]+iva
    print(indice,listado,precios[indice], "+ iva:", total)
    
