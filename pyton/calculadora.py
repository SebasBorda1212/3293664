#calculadora basica

"""
(1) suma
(2) resta
(3) multi
(4) divi
"""
def calculadora(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    else:
        print("T equivocaste de opcion")

print (calculadora(40,23,3))
   