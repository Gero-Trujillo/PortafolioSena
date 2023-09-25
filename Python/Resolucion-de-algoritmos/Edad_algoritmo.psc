Algoritmo Edad_algoritmo
	definir dia, mes, año, dia_n, mes_n, año_n, edad como entero
	escribir"Ingrese su fecha de nacimiento"
	escribir "Dia: ";leer dia_n
	escribir "Mes: ";leer mes_n
	escribir "Año: ";leer año_n
	escribir "Ingrese la fecha de hoy"
	escribir "Dia: ";leer dia
	escribir "Mes: ";leer mes
	escribir "Año: ";leer año
	si mes >= mes_n Entonces
		si dia >= dia_n Entonces
			edad = año-año_n
			escribir "Su edad actual es: ",edad
		SiNo
			edad = año-año_n-1
			escribir "Su edad actual es: ",edad
		FinSi
	SiNo
		edad = año-año_n-1
		escribir "Su edad actual es: ",edad
	FinSi

FinAlgoritmo
