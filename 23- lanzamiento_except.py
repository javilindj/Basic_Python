'''def evaluaEdad(edad):

	if edad<0:
		raise TypeError("No puedes introducir una edad negativa")
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65: 
		return "eres un boomer"
	elif edad<100:
		return "cuídate"

print(evaluaEdad(-6))'''
import math

def calculaRaiz(n1):
	if n1<0:
		raise ValueError("El número no puede ser menor a 0")
	else:
		return math.sqrt(n1)

op1=int(input("Introduce un número: "))

try:
	print(calculaRaiz(op1))

except ValueError as ErrorNumerNegativo:
	print(ErrorNumerNegativo)

print("Programa ha finalizado")