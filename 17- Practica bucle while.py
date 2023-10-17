#Ejercicio 1: Crea un programa que pida número infinitamente de manera ascendente, si introduces uno menor al anterio finaliza.
'''numero=int(input("Introduce un número, por favor: "))

num=0

while numero>num:
	numero=int(input("Introduce un número, por favor: "))
	num=num+1

if numero<=num:
	print("El programa ha finalizado")'''

#Ejercicio 2: Crea un programa que pida nº pos

numero=int(input("Introduce un número, por favor: "))

suma = 0

while numero>0:
	suma=suma+numero
	numero=int(input("Introduce un número, por favor: "))
	

print("la suma de los números es: ", str(suma))





	
