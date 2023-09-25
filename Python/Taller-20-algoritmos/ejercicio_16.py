n = int(input("Ingrese el numero: "))

a = 0
b = 1
listF = []

print(f"Los primeros {n} de la serie Fibonacci son:")
for i in range(n):
    c = a + b
    a = b
    b = c
    listF.append(a)

listF.reverse()
for dato in listF:
    print(dato)