nombre = input("Ingrese su name: ")
vocales = ["a", "e", "i", "o", "u"]
lista = []
dicc = {}
for letra in (nombre):
    if letra in vocales:
        if letra in lista:
            continue
        else:
            lista.append(letra)
            dicc[letra] = nombre.count(letra),"veces"
            print(f"La letra {letra} está {nombre.count(letra)} veces")

print(dicc)    
        

