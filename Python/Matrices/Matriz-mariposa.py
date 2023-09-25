#Matriz en forma de mariposa

n = int(input("Ingrese el tamaño de la matriz (impar): "))
matriz = [[1] * n for _ in range(n)]
aux = n-1
for i in range(n):
    for j in range(n):
        if i <= j < n - i or i >= j > n - i - 2:
            matriz[i][j] = 0
            if i == j:
                matriz[i][j] = 1
            if j == aux:
                matriz[i][j] = 1
                aux -= 1

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()


