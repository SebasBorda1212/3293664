from menu import mostrar_menu
from personaje import crear_personaje, ver_personaje
from batalla import batalla

personaje = {}

while True:
    mostrar_menu()
    op = input("Opción: ")

    if op == "1":
        personaje = crear_personaje()
    elif op == "2":
        ver_personaje(personaje)
    elif op == "3":
        batalla(personaje)
    elif op == "4":
        print("Saliendo del juego...")
        break
    else:
        print("Opción inválida.")
