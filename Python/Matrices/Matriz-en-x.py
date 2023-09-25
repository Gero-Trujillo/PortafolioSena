'''Este programa solicita al usuario un numero entero el cual será tamaño de la matriz cuadrada
luego crea la matriz, pero esta se imprimirá en forma de X con numeros en orden ascendente. Los
demas espacios fuera de la X se rellenan con 0'''

n = int(input("Ingrese tamaño de la matriz cuadrada: "))
matriz = []
valor1 = 0
valor2 = 1
aux = n-1
for i in range(n):
    for j in range(n):
        if j == aux:
            print(valor2, end=" ")
            valor2+=1
            aux-=1
        elif i == j:
            print(valor2, end=" ")
        else:
            print(valor1,end=" ")
    print()