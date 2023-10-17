class Persona():
	def __init__(self,nombre,edad,residencia):
		self.nombre=nombre
		self.edad=edad
		self.residencia=residencia

	def descripcion(self):

		print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nResidencia: ",self.residencia)

class empleado(Persona):
	def __init__(self,salario,tiempo,nombre_empleado,edad_empleado,residencia_empleado):
		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
		self.salario=salario
		self.tiempo=tiempo

	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario,"\nAntigüedad: ",self.tiempo)

Antonio=empleado(1500,15,"Manuel",55,"Colombia")
Antonio.descripcion()

print(isinstance(Antonio, empleado))