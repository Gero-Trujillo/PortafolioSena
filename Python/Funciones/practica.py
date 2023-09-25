def suma_ab():
    a = 5
    b = 10
    c = a+b
    print(c)

def esPar(n):
    if n%2==0:
        return True
    else:
        return False

def esPrimo(n):
    for i in range(2, n-1):
        if n%i==0: return False
    return True

def raiz(n):
    res = n**0.5
    print(f"la raiz de {n} es {res}")

def tabla():
    n = int(input("Ingrese la tabla que dese ver: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")


def tablas_3():
    for i in range(1, 11):
        print(f"{i} x 1 = {i * 1}", end="\t")
    
        print(f"{i} x 2 = {i * 2}", end="\t")
    
        print(f"{i} x 3 = {i * 3}")

def factorial():
    n = int(input("ingrese el numero: "))
    acu = 1
    for i in range(1,n+1):
        acu = acu*i
    print(acu)

def sumita():
    a = 5
    b=3
    return a+b
print(sumita())

def m_cal(a,b):
    multip=a*b
    suma=a+b
    resta=a-b
    return f"La suma es {suma}, la resta es {resta}, la multiplicación es {multip}" 
a = int(input("Ingrese numero: "))
b = int(input("Ingrese numero: "))
print(m_cal(a,b))

def name_comp():
    n_ap = input("Ingrese su primer nombre: ")
    p_n = input("ingrese el 1er nombre del padre: ")
    p_a = input("Ingrese el 1er apellido del padre: ")
    m_n = input("ingrese el 1er nombre de la madre: ")
    m_a = input("Ingrese el 1er apellido de la madre: ") 
    return f"{n_ap} {p_a} {m_a}"
print(name_comp().upper())


def facto(n):
    if n<2:
        return 1
    else:
        return n*facto(n-1)
n=int(input("Ingrese n: "))
print(facto(n))

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

print("Bienvenido calidad")

print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. potenciacion")
print("6. porcentaje")
print("7. raiz")
print("8. logritmo")
op = int(input("Presiona la operacion: "))
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




"""n = int(input("Ingrese n: "))
raiz(n)"""
        
       
"""n = int(input("Ingrese el numeo a comprobar: "))
if esPrimo(n):
    print(f"{n}, es primo")
else:
    print(f"{n}, no es primo")"""