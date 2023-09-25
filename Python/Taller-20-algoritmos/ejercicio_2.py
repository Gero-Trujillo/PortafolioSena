a = int(input("Ingrese el nuemro: "))
b = int(input("Ingrese el nuemro: "))
c = int(input("Ingrese el nuemro: "))
d = int(input("Ingrese el nuemro: "))
lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.sort(reverse=True)
for dato in lista:
    print(dato)