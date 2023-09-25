import math
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def pot(a,b):
    return a**b
def porcentaje(a,b):
    return (a/100)*b
def raiz(a):
    return math.sqrt(a)
def log(a):
    return math.log10(a)

print("Bienvenido")

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. potenciacion")
print("6. porcentaje")
print("7. raiz")
print("8. logritmo")
print("0. Salir")
op = int(input("Presiona la operacion: "))
while op != 0:
    if op==1:
        a=int(input("Ingrese numero: "))
        b=int(input("Ingrese numero: "))
        print(suma(a,b))
    elif op==2:
        a=int(input("Ingrese numero: "))
        b=int(input("Ingrese numero: "))
        print(resta(a,b))
    elif op==3:
        a=int(input("Ingrese numero: "))
        b=int(input("Ingrese numero: "))
        print(multi(a,b))
    elif op==4:
        a=int(input("Ingrese numero: "))
        b=int(input("Ingrese numero: "))
        print(div(a,b))
    elif op==5:
        a=int(input("Ingrese numero: "))
        b=int(input("Ingrese exponente: "))
        print(pot(a,b))
    elif op==6:
        a=int(input("Ingrese numero: "))
        b=int(input("El porcentaje que desea: "))
        print(porcentaje(a,b))
    elif op==7:
        a=int(input("Ingrese numero: "))
        print(raiz(a))
    elif op==8:
        a=int(input("Ingrese numero: "))
        print(log(a))
    op = int(input("Presiona la operacion: "))