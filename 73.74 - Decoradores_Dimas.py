# https://www.youtube.com/watch?v=ubJMrnzuc0c - vídeo

""" Apartado 1: Las funciones son objetos
Por tanto
- Es una instacia de tipo objeto
- Podemos almacenar una función en una variable
- Podemos pasa una función como parámetro de otra función
- Una función puede retornar en otra función
- Se pueden almacenar en estructuras de datos, tablas, listas...

"""
def funcíon_Externa(nombre):
	def funcionEnvoltorio():
		print("\nEmpieza la función envoltorio")
		print(nombre)
		print("\nFinal de la función envoltorio")

	return funcionEnvoltorio

instanciaFuncion = funcíon_Externa("Javi")
instanciaFuncion()
otra_funcion = funcíon_Externa("Aroa")
otra_funcion()
print(otra_funcion.__name__) #.__name__


""" Apartado 2: 
- Función como argumento de otra función
- En vez de pasar la variable "nombre", pasaremos otra función.
"""
from datetime import datetime

def fecha():
	print(datetime.today().strftime("%d-%m-%Y"))
fecha()

def hora():
	print(datetime.now().strftime("%H:%M:%S"))
hora()

def funcionExt(funcionInt):
	def funcionEvn():
		print("\nEmpieza la función")
		funcionInt()
		print("\nFin de la función")
	return funcionEvn

"""mostrarHora = funcionExt(hora)
mostrarFecha = funcionExt(fecha)
mostrarHora()
mostrarFecha()"""

"""Apartado 3:Sintaxtis de los Decoradores:
"""

def funcionExt(funcionInt):
	def funcionEvn():
		print("\nFunción sintaxis")
		funcionInt()
		print("\nAcaba la función sintaxis")
	return funcionEvn

@funcionExt
def saludar():
	print("Hola crack")

@funcionExt
def despedirse():
	print("Adiós máquina")
saludar()
despedirse()

""" Apartado 4: Funciones con argumentos
Veremos cómo podemos usar decoradores con funciones
que reciban diferentes número de argumentos
"""

def sumarNumeros(*args,**kwargs):
	acc = 0
	for num in args:
		acc += num
	return acc
print("El resultado de la suma es: ",sumarNumeros(1,2,3,4,5,6,7,8,9,10))
def operarConPares(operacion):
	def wrapper(*args,**kwargs):
		soloPares = list(filter(lambda num: num%2 == 0,args))
		resultado = operacion(*soloPares,**kwargs)
		print(f"El resultado de la operación es: {resultado}")
		return resultado
	return wrapper

sumarPares = operarConPares(sumarNumeros)
print(sumarPares(1,2,3,4,5,6)) # Suma 2+4+6 que son 12

@operarConPares
def multiplicar(*args,**kwargs):
	acc = 1
	for num in args:
		acc *= num
	return acc
multiplicar(1,2,3,4)

#Reto:
""" tenemos que en la función de multiplicar tenemos que devolver el resultado de la
multimplicación con un valor máximo variable, jugando con los kargs """
