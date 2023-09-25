x = float(input("Ingrese el valor de (x): "))
y = 3 * x + 2
while y != 0:
    print("El valor de (y) para (x) = ", x, " es: ", y)
    x = float(input("El valor de (y) no es igual a 0, ingrese otro valor de (x): "))
    y = 3 * x + 2
    
print("El valor de (y) para (x) = ", x, " es: ", y)