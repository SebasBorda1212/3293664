# Ejercicio 29 : Primos hasta 50
def es_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
primos = [n for n in range(2,51) if es_primo(n)]
print(primos)
