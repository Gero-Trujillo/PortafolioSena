n = int(input("Ingrese un numero mayor a 3 cifras: "))
if n>999:
    a = str(n)
    a_invertido = (a[::-1])
    n_invertido = int(a_invertido)
    print(n_invertido)
else:
    print("El numero ingresado no es mayor a 3 cifras, intente de") 