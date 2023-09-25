a = float(input("Ingrese el valor del angulo a: "))
b = float(input("Ingrese el valor del angulo b: "))
while a+b >= 180:
    print("Valores incorrectos")
    a = float(input("Ingrese el valor del angulo a: "))
    b = float(input("Ingrese el valor del angulo b: "))
ab = a+b
c = 180 - ab
if a==90 or b==90 or c==90:
    print("El angulo restante es: ",c, " y SI es un triangulo rectangulo")
else:
    print("El angulo restante es: ",c, " y NO es un triangulo rectangulo")