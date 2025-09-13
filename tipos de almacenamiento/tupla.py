#tupla

tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
tupla2 = "Laura", "Camilo", "Valentina"
nuevalista = tupla
print(tupla[5])
print(tupla2)
print(nuevalista)

tupla3 = tuple([99, 15, 77, 33, 5])
ordenada = sorted(tupla3)
print(tupla3)
print(ordenada)

tupla4 = ('Sofía', 25, 'México')
nombre, edad, nacionalidad = tupla4
print(nombre)
print(edad)
print(nacionalidad)

tupla5 = ((11, 22), (33, 44), (55, 66))
print(tupla5[2][0])

tupla1 = (4, 4, 4)
tupla2 = (4, 4, 4)

tupla3 = (8, 8, 8)
tupla4 = (2, 2, 2)

print(tupla1 == tupla2)
print(tupla1 > tupla2)
print(tupla1 < tupla2)

print(tupla3 == tupla4)
print(tupla3 > tupla4)
print(tupla3 < tupla4)