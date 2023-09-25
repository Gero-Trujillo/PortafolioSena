from collections import Counter
import random
a = set()
b = set()
lista=[]
for i in range(random.randint(1,10)):
    n = random.randint(0,9)
    a.add(n)
    lista.append(n)
for j in range(random.randint(1,10)):
    n = random.randint(0,9)
    b.add(n)
    lista.append(n)
print(f'Conjunto a (cardinalidad): {a}');print(f'Conjunto b (cardinalidad): {b}')
"""print(f"diferencia de a - b {a-b}")
print(f"diferencia de b -a {b-a}")
print(f"a | b {a | b}")
print(f"a^b {a ^ b}")
print(f"a & b {a & b}")"""

conteo = Counter(lista)

resul = {}
for clave in conteo:
    valor = conteo[clave]
    if valor != 0:
        resul[clave] = valor
print(f'Dicciionario de cantidad que se repite un numero {resul}')
print(f"esta es la lista con todo los numeros {lista}")