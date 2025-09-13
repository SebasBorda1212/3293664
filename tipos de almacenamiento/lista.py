# lista

numeros = [2, 9, 14, 21, 32, 45, 55, 6, 19]

def saludar(nombre):
    print("Hola, Python te dice hola", nombre)

saludar("Laura")

def num(numeros):
    print(numeros)

num(numeros)

diccionario = [
    {"nombre": "Laura", "edad": 23, "ciudad": "Chía"},
    {"nombre": "Mateo", "edad": 19, "ciudad": "Zipaquirá"},
    {"nombre": "Juliana", "edad": 28, "ciudad": "Cota"},
    {"nombre": "Felipe", "edad": 16, "ciudad": "Tabio"},
    {"nombre": "Valeria", "edad": 21, "ciudad": "Tenjo"},
    {"nombre": "Sebastián", "edad": 12, "ciudad": "La Calera"},
]

for i in range(0, 6):
    val = diccionario[i]["nombre"]
    print(val)

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

archivo = open("Dic.txt", "a")
archivo.write(nombre + ", " + str(edad) + "\n")
archivo.close()