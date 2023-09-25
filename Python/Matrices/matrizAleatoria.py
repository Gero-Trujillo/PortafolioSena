import random
#Creamos una variable n con un valor random y creamos la amtriz llena de ceros
n = random.randint(2,9)
matriz = [[0 for _ in range(n)]for _ in range(n)]

# Llenar matriz con valores random en un rango random
for fila in range(n):
    for columna in range(n):
        valor = random.randint(0,9)
        matriz[fila][columna]=valor
        
#imprimimos n, para saber cual es su valor y comprobar que esté bien el tmaaño de la matriz
print("Valor de (n) es: ", n)

#Matriz normal
print("matriz normal")
for i in matriz:
    for j in i:
        print(j, end=" ")
    print()
    
print("-------------------------")

print("matriz reverso")
#Matriz reverso
for fila in range(n):
    for columna in range(n):
        print(matriz[columna][fila], end=" ")
    print()