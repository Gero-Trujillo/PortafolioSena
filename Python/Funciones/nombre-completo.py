#Solicita datos y imprime el nombre completo

def name_comp():
    n_ap = input("Ingrese su primer nombre: ")
    p_n = input("ingrese el 1er nombre del padre: ")
    p_a = input("Ingrese el 1er apellido del padre: ")
    m_n = input("ingrese el 1er nombre de la madre: ")
    m_a = input("Ingrese el 1er apellido de la madre: ") 
    return f"{n_ap} {p_a} {m_a}"
print(name_comp().upper())