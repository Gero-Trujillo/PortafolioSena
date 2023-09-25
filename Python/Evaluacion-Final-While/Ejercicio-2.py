'''En este problema debes implementar el bucle While y la llamada de funciones. Existen 
tres campamentos ubicados en un plano y con coordenadas cartesianas. Las 
ubicaciones las escoge el usuario ingresando valores en forma de tuplas (x,y)¸con x, 
y como enteros. Las ubicaciones de los campamentos deben formar un triangulo y, 
no pueden estar alineados los tres. EL usuario debe ingresar un punto de 
abastecimiento dentro del área triangular formada por los campamentos. Se debe 
crear un programa que pida las tres ubicaciones en forma de tuplas (x,y), y un 
cuarto punto de abastecimiento, el programa debe validar que las coordenadas 
de los tres campamentos no sean lineales para luego pedir el punto de 
abastecimiento. EL programa enviará mensaje de error en caso de que los tres 
puntos iniciales sean colineales y/o en caso en que el cuarto punto de 
abastecimiento no esté dentro del área triangular. POR ÚLTIMO, EL PROGRAMA 
DEBERÁ CALCULAR E IMPRIMIR LA MENOR DISTANCIA DESDE CADA 
CAMPAMENTO HASTA EL LUGAR DE ABASTECIMIENTO.'''


def dife(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def punto_dentro(p, p1, p2, p3):
    d1 = dife(p, p1, p2)
    d2 = dife(p, p2, p3)
    d3 = dife(p, p3, p1)
    
    hay_nega = (d1 < 0) or (d2 < 0) or (d3 < 0)
    hay_posi = (d1 > 0) or (d2 > 0) or (d3 > 0)

    if hay_nega and hay_posi:
        return False
    else:
        return True
def colineal(p1, p2, p3):
    m1 = (p2[1]-p1[1])/(p2[0]-p1[0]) if (p2[0]-p1[0]) != 0 else float()
    m2 = (p3[1]-p1[1])/(p3[0]-p1[0]) if (p3[0]-p1[0]) != 0 else float()
    if m1 == m2:
        return False
    else:
        return True

def distancia(x,y):
    return ((y[0] - x[0])**2 + (y[1] - x[1])**2)**0.5

def distanciaAbaste(p1, p2, p3, p):
    print(f"Distancia p1 y p: {distancia(p1,p)}")
    print(f"Distancia p2 y p: {distancia(p2,p)}")
    print(f"Distancia p3 y p: {distancia(p3,p)}")
    
    
p1 = (int(input("Numero x1: ")), int(input("Numero y1: ")))
p2 = (int(input("Numero x2: ")), int(input("Numero y2: ")))
p3 = (int(input("Numero x3: ")), int(input("Numero y3: ")))
if colineal(p1, p2, p3):
    p = (int(input("Numero del punto xp: ")), int(input("Numero del punto yp: ")))
    if punto_dentro(p, p1, p2, p3):
        print("La coordenada del punto está dentro del triángulo.")
    else:
        print("La coordenada del punto está fuera del triángulo.")
else:
    print("¡ERROR!. Las coordenadas son colineales")
    exit()
    
distanciaAbaste(p1, p2, p3, p)
