def generar_factura(comprador, seleccion, productos, precios):
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
