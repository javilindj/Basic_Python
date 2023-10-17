#---Ejemplo de Pogramación orientada a objetos---
#---Creamos la clase con las propiedades y su correspondiente valor---
class Coche():

	def __init__(self): # con el init declaramos el estado inicial y en cada propiedad tenemos qque añadir el self.

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 # Añadiendo __ la encapsulamos para protegerla para que no se pueda modificar fuera de la clase, si se puede modificar desde un método dentro de la clase.
		self.__enmarcha=False

	def arrancar(self, arrancamos): #---Método, es similar a una función pero solo los métodos pueden estar dentro de una clase. 
		self.__enmarcha=arrancamos
		
		if(self.__enmarcha):
				chequeo=self.__chequeo_interno()
		
		if (self.__enmarcha and chequeo):
			
			return "El coche está en marcha"
		
		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo, no podemos arrancar"

		else:
			return "El coche está parado"

		self.enmarcha=True

	def estado(self):
		print("El coche tiene " ,self.__ruedas, "ruedas. Un acho de ", self.__anchoChasis, "y un largo de ",
		 self.__largoChasis)
		
	def __chequeo_interno(self):
		print("Realizando chequeo interno")
		
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False

miCoche=Coche() #--- Instanciar la clase

print(miCoche.arrancar(True))

miCoche.estado()


print("---------A continuación creamos el segundo objeto-------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()
