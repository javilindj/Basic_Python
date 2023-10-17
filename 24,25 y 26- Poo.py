#---Ejemplo de Pogramación orientada a objetos---
#---Creamos la clase con las propiedades y su correspondiente valor---
class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

	def arrancar(self): #---Método, es similar a una función pero solo los métodos pueden estar dentro de una clase. 
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "El coche está en marcha"

		else:
			return "El coche está parado"

miCoche=Coche() #--- Instanciar la clase

print("El largo de el coche es: ",miCoche.largoChasis)
print("El coche tiene: ",miCoche.ruedas, "ruedas")
#miCoche.arrancar()
 
print(miCoche.estado())