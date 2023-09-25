def esPrimo(num):
    for i in range(2, num-1):
        if num%i==0: return False
    return True

def primoSup(n):
    num = n + 1
    while True:
        if esPrimo(num):
            return num
        num += 1

n = int(input("Ingrese un valor entero positivo: "))
if n <= 0:
    print("El valor ingresado debe ser positivo.")
primoSup = primoSup(n)
print(f"El primer número primo superior a {n} es: {primoSup}")
