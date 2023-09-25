#Numero binario aleatorio y luego lo convierte a decimal

import random
lista=[]
for i in range(random.randint(2,10)):
    binario_aleatorio = random.randint(0,1)
    lista.append(binario_aleatorio)
expo= len(lista)
lista2=[]
for num in lista:
    resultado=(2**expo)*num/2
    lista2.append(resultado)
    expo-=1
listaRes=sum(lista2)
print(f"""el numero binario es: {(''.join(map(str, lista)))} 
el numero entero es: {(int(listaRes))}""")