edadAp = {'johao': 23,  'adrian':16, 'daya':25, 'juli':17, 'ossa':16}
valores = edadAp.values()
llave = edadAp.keys()
llave_orden=sorted(llave)
ordenado={}
mayores={}
menores={}
for key in llave_orden:
    ordenado[key] = edadAp[key]
for llave,valor in ordenado.items():
    if valor >= 18:
        mayores[llave] = valor
    else:
        menores[llave] = valor
for i,j in mayores.items():
    print(f"Es mayor de edad su nombre es {i} y tiene {j} años")
for i,j in menores.items():
    print(f"Es menor de edad su nombre es {i} y tiene {j} años")
