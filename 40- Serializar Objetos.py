import pickle

class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enmarcha,
			"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

coche1=Vehiculos("Seat","Ibiza")
coche2=Vehiculos("Tesla","Model S")
coche3=Vehiculos("BMW","Serie 3")

coches=[coche1,coche2,coche3]

fichero=open("losCoches","wb")
pickle.dump(coches, fichero)

del (fichero)

ficheroApertura=open("losCoches","rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for b in misCoches:

	print(b.estado())