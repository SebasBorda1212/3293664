# Ejercicio 32 : Buscar números en texto
import re
texto = "Tengo 2 perros y 3 gatos"
print(re.findall(r'\d+', texto))
