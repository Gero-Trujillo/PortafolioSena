n = int(input("Ingrese un numero: "))
a = str(n)
acum = 0
a_dig = (a[0::1])
for digito in a_dig:
    print(digito)
for digito in a_dig:
    acum = acum+ int(digito)
print("La suma de los digitos es: ")
print(acum)