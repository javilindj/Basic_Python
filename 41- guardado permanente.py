import pickle

class Persona:
	def __init__(self,nombre,genero,edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva llamada -->",self.nombre)

	def __str__(self):
		return "{}{}{}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:

	personas=[]

	def __init__(self):

		listaDePersonas=open("ficheroExterno","ab+")
		listaDePersonas.seek(0)
		
		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} peronas en el fichero".format(len(self.personas)))
		
		except:
			print("El fichero está vacío")
		
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self,p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas,listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarinfoficheroexterno(self):
		print("La información del fichero externo es la siguiente")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()
persona=Persona("Javi" ,"Masculino", 39)
miLista.agregarPersonas(persona)
miLista.mostrarinfoficheroexterno()
