#imprtar contactos a agenda

from contactos import contactos

def guardar_contactos(contactos_dict):
    with open("data.txt", "w", encoding="utf8") as data:
        for nombre, telefono in contactos_dict.items():

            
            data.write(f"{nombre}: {telefono}\n")

while True:
    print("""
        ¡Agenda de contactos!    
          Menú interactuable
    ==============================
          1. Agregar contacto
          2. Consultar contacto
          3. Actualizar contacto
          4. Eliminar contacto
          5. Visualizar agenda completa
          6. Salir
    ==============================
    """)

    opcion = int(input("Ingrese el número de la acción a realizar: "))

    if opcion == 1:
        nombre = input("Ingrese nombre del contacto: ").strip()
        if nombre in contactos:
            print("Este contacto ya existe.")
        else:
            telefono = input("Ingrese el número telefónico: ")
            contactos[nombre] = telefono
            print("Contacto agregado correctamente.")
            guardar_contactos(contactos)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del contacto a consultar: ").strip()
        if nombre in contactos:
            print(f"{nombre}: {contactos[nombre]}")
        else:
            print("Contacto no encontrado.")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del contacto a actualizar: ").strip()
        if nombre in contactos:
            nuevo_telefono = input("Ingrese el nuevo número telefónico: ")
            contactos[nombre] = nuevo_telefono
            print("Contacto actualizado.")
            guardar_contactos(contactos)
        else:
            print("Contacto no encontrado.")

    elif opcion == 4:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
        if nombre in contactos:
            del contactos[nombre]
            print("Contacto eliminado.")
            guardar_contactos(contactos)
        else:
            print("Contacto no encontrado.")

    elif opcion == 5:
        if contactos:
            print("\nAgenda completa:")
            for nombre, telefono in contactos.items():
                print(f"{nombre}: {telefono}")
        else:
            print("La agenda está vacía.")

    elif opcion == 6:
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")