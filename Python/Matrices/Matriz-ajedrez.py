import random

n = random.randint(12, 120)

matriz = [n, n]

for filas in range(n):
    for columnas in range(n):
        if (filas // 4 + columnas // 4) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
print(matriz)

