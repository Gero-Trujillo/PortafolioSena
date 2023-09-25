"""lista = []
while len(lista)<4:
    valor = input("Ingrese el valor: ")
    lista.append(valor)
print(lista)"""
import random
n = int(input("ingrese n: "))
matriz = []
i = 0
while i < n:
    j=0
    while j < n:
        valor = random.randint(0,9)
        matriz.append(valor)
        print(valor, end=" ")
        j+=1
    i+=1
    print()

    

