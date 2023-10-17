'''i=1

while i<=10:
	print("Ejecución" + str(i))
	i=i+1

print("Terminó la Ejecución")'''
'''
edad=int(input("Introduce la edad, por favor: "))

while  edad<0 or edad>120:
	print("Has introducido una edad incorrecta, vuelve a intentarlo")
	edad=int(input("Introduce la edad, por favor: "))

print("Gracias por colaborar")
print("Edad del aspirante: " + str(edad))'''
import math

print("Programa de cálculo de raìz cuadrada")
numero=int(input("Introduce un número, por favor: "))

intentos=0

while numero <0:
	print("No se puede hallar la raìz cuadrada de un número negativo")

	if intentos==2:
		print("Has consumido demasiados intentos, el programa ha finalizado")
		break;
	numero=int(input("Introduce un número, por favor: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("la raiz cuadarada de " + str(numero) + " es " + str(solucion))

print("Programa edades")
edad=int(input("Introduce tu edad, por favor: "))

while edad<5 or edad>100:
	print("Has introducido una edad incorrecta, introduce tu edad de nuevo: ")
	edad=int(input("Introduce tu edad, por favor: "))

print(f"La edad del usuario es: " + str(edad))

