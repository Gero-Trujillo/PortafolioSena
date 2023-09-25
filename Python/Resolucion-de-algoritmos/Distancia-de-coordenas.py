x1 = int(input("Ingresá x1: "))
y1 = int(input("Ingresá y2: "))
x2 = int(input("Ingresá x2: "))
y2 = int(input("Ingresá y2: "))
x3 = int(input("Ingresá x3: "))
y3 = int(input("Ingresá y3: "))
x4 = int(input("Ingresá x4: "))
y4 = int(input("Ingresá y4: "))

distancia = ((x2 - x1)**2 + (y2-y1)**2)**0.5
print(distancia)

z1 = (y2-y1)/(x2-x1) if (x2-x1) != 0 else float()
z2 = (y3-y1)/(x3-x1) if (x3-x1) != 0 else float()

if z1 == z2:
    print("Son lineales")
else:
    print("No son lineales")
    