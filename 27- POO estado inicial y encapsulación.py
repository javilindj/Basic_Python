#---Ejemplo de Pogramación orientada a objetos---
#---Creamos la clase con las propiedades y su correspondiente valor---
class Coche():

	def __init__(self): # con el init declaramos el estado inicial y en cada propiedad tenemos qque añadir el self.

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 # Añadiendo __ la encapsulamos para protegerla para que no se pueda modificar fuera de la clase
		self.__enmarcha=False

	def arrancar(self, arrancamos): #---Método, es similar a una función pero solo los métodos pueden estar dentro de una clase. 
		self.__enmarcha=arrancamos
		if (self.__enmarcha):
			return "El coche está en marcha"

		else:
			return "El coche está parado"

		self.enmarcha=True

	def estado(self):
		print("El coche tiene " ,self.__ruedas, "ruedas. Un acho de ", self.__anchoChasis, "y un largo de ",
		 self.__largoChasis)
		
			

		

miCoche=Coche() #--- Instanciar la clase
print(miCoche.arrancar(True))

miCoche.estado()

print("---------A continuación creamos el segundo objeto-------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()