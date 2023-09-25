n = int(input("Ingrese el numero: "))
while n%17 != 0:
    print(n,", NO es multiplo de 17")
    n = int(input("Ingrese otro numero: "))
print(n,", SI es multiplo de 17")