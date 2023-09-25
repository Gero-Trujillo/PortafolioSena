an = input("Ingrese si el año es bisiesto o normal: ")
fest=int(input("ingrese cuantos festivos tiene el año: "))
fs=int(input("ingrese cuantos fines de semana viaja a sopetran: "))
import math
fsd = 36
festd = fest/4 * 3
if an == "bisiesto":
    pjp = fsd+festd
    pjb = pjp*0.15
    pj= pjp+pjb
    redondeado = math.floor(pj)
    print(f"la cantidad de veces que jugó en el año es: {redondeado}")
else:
    pj= fsd+festd
    redondeado = math.floor(pj)
    print(f"la cantidad de veces que jugó en el año es: {redondeado}")