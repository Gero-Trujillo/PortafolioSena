#Loteria aletaoria

import random
dicc_lot = {'lunes':'medellin', 'martes':'astroluna', 'miercoles':'risaralda', 'jueves':'paisita', 'viernes':'cafeterito'}
values = dicc_lot.items()
alea = random.choice(list(values))
print(alea)