n = int(input("Ingrese un numero: "))
i = 1
acum = 1
while i<=n:
    acum = acum*i
    i += 1
print("El factorial de ",n," es: ",acum)