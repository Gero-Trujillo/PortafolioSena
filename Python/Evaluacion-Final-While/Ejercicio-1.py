'''En este problema has de implementar el bucle While y la llamada de funciones debes 
construir un algoritmo en Python que solicite al usuario un valor entero positivo ‘n’ y 
luego mostrará el termino n-ésimo de la serie Fibonacci, la cual en este caso iniciará 
en 11 y su segundo término será 12.
Datos de ejemplo si el usuario ingresa n=4 tenemos que Fb(4): 35
Los primeros 5 valores de la serie son: 11,12,23,35,58, 93'''

def fibo(n):
    a = 11
    b = 12
    i = 1
    while i <= n-1:
        c = a + b
        a = b
        b = c
        i += 1
    print(a)
n = int(input("Ingrese n: "))
fibo(n)