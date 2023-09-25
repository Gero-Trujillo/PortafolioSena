'''Este programa solicita al usuario el tamaño de la matriz(filas y columna),
posteriormente solicita cada uno de los valores de la matriz y comprobará
si la suma de sus digitos son pares, de ser asi invierte el numero de lo
contrario lo deja normal'''

x = int(input("Cuantas filas tiene la matriz: "))
y = int(input("Cuantas columnas tiene la matriz: "))
matriz = [[0 for _ in range(y)]for _ in range(x)]
for i in range(x):
    for j in range(y):
        valor = int(input(f"Ingrese el valor {i},{j}: "))
        matriz[i][j] = valor
for i in matriz:
    for num in i:
        suma = 0
        if "-" in str(num):
            for dig in str(abs(num)):
                suma += int(dig)
            if suma%2==0:
                num = str(num)
                num_rev = num[-1:0:-1]
                print(f"-{num_rev}", end=" ")
            else:
                print(num, end=" ")
        else:
            for dig in str(num):
                suma+=int(dig)
            if suma%2==0:
                num = str(num)
                num_rev = num[::-1]
                print(num_rev, end=" ")
            else:
                print(num, end=" ")
    print()
