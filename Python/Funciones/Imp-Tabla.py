#Imprimir cualquier tabla de multiplicar

def tabla():
    n = int(input("Ingrese la tabla que dese ver: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")