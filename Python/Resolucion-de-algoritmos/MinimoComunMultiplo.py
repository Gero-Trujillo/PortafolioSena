#encontrar minimos comun multiplo de 2 numeros

def mcm():
    num1, num2 = v1, v2
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    mcm = (v1*v2) // num1
    return mcm

v1 = int(input("Ingresa numero 1: "))
v2 = int(input("Ingresa numero 2: "))
print(mcm())