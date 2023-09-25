import match
usuario = input("Ingrese el usuario: ")
clave = input("Ingresa la contraseña: ")

match usuario, clave:
   case 'gero', '511':
      print("Bienvenido!!")
      exit()
   case _:
      print(f"Usuario o contraseña incorrecta")
      exit()   
