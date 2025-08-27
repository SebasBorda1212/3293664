equipos_Colombianos=["Millonarios","Nacional","SantaFe","Junior","OnceCaldas"]
equipos_Colombianos.append("Pereira")
print (equipos_Colombianos)
equipos_Colombianos.insert(2,"Fortaleza")
print (equipos_Colombianos)

equipos_Colombianos.append("Bucaramanga")
print(equipos_Colombianos)
equipos_Colombianos.extend({"Cartagena","Equidad","Amazonas"})
print(equipos_Colombianos)

#equipos_Colombianos.remove("Nacional")
#print(equipos_Colombianos)
#equipos_Colombianos.pop(2)
#print(equipos_Colombianos)
#for primera_division in equipos_Colombianos:
#    print(primera_division)
#for indice, primera_division in enumerate(equipos_Colombianos):
#    print(indice,primera_division)
#for primera_division in range(len(equipos_Colombianos[2:6])):
#    print(primera_division)

print (len(equipos_Colombianos))
print(len(equipos_Colombianos[0]))
var="millos"in equipos_Colombianos
print(var)  
var2="Millonarios"in equipos_Colombianos
print(var2  )
var3="coundksnfknsz"
var4= var3.count("k")
print(var4)
