def esPrimo(num):
    for i in range(2, num-1):
        if num%i==0: return False
    return True

def primos_descendente(n):
    primos = []
    num = 2
    while len(primos) < n:
        if esPrimo(num):
            primos.append(num)
        num += 1
    return primos

n = int(input("Ingrese la cantidad de primos que desea encontrar: "))
if n > 0:
    primos = primos_descendente(n)
    primos.reverse()
    print(f"Los pimeros {n} numero primos son:")
    for primo in primos:
        print(primo)
else:
    print("El valor debe ser un entero mayor a 0")
