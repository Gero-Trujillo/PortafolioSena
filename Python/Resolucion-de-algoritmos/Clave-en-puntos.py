"""diccionario={
    "nombre":"julian",
    "apellido":"posso",
    "edad":17,
    "nombre2":"gero",
    "apellido2":"trujillo",
    "edad2":18
}

for value in diccionario.values():
    print(value)"""
import stdiomask
dic = {
    "usuario":"gero",
    "clave":"gero12345"
}
intentos = 0
rest=3
while intentos < 3:
    user = input("Ingrese usuario: ")
    clave = stdiomask.getpass("ingrese clave: ")
    if user == dic["usuario"] and clave == dic["clave"]:
        print("Bienvenido amistad")
        exit()
    else:
        print(f"usuario o clave incorrecta, te quedan {rest-1} intentos")
        intentos+=1
        rest-=1
print("numero de intentos excedido, intende mas tarde")
exit()



