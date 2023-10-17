print("Programa de valoracion de alumnos") # Titulo que nos muestra al abrir la consola

nota_alumno=input("Introduce la nota de usuario :") # variable que recibe parámetros de tipo strings,int(input) para recibir tipo entero

def evaluación(nota): # Función que nos pide un parámetro

	valoracion="aprobado" # La variable por defecto da aprobado, si entra en condicional y cumple que es menor de 5 nos dará suspenso
	if nota <5:
		valoracion="suspenso"
	return valoracion

print(evaluación(int(nota_alumno)))
'''Le indicamos en el print que nos devuelva el resultado de la nota,
 al introducir en la consola un valor de tipo entero y estar preparada para para strings debemos añadir int()
 sino nos dará una excepción por no estar preparada para recibir un valor de tipo entero'''
