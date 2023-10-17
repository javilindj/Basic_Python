#Verificar que los elementos de una lista cumplan una determinada condición.
#------ Ejemplo con funcion -----

emails = [
"javi@msn.com",  "pedro@mm.es","jose","jops","peter@"]
def evaluaEmail(email):
	return '@' in email

#------- Ejemplo con lambda-------

emailValidos = list(filter(lambda email:'@' in email, emails))
print(emailValidos)


#----------------------------------------
edades = [12,11,33,21,15,18,32,7]

def mayorEdad(edad):
	return edad>=18

#filter(mayorEdad,edades)
edadesmayores = tuple(filter(mayorEdad,edades))
print(f"Los mayores de edad son:", edadesmayores)
#---------------------------------------

numeros=[12,22,21,87,92]
numerosPar = list(filter(lambda numero_par:numero_par%2==0,numeros))
print(f"Los números pares son: ", numerosPar)

#-----------------------------------

class Empleado:

	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario


	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)

ListaEmpleados=[
Empleado("Juan","Director",75000),
Empleado("Ana","Presidenta",85000),
Empleado("Antonio","Administrativo",25000),
Empleado("Sara","Secretaria",27000),
Empleado("Mario","Botones",21000)
]
salario_altos=list(filter(lambda empleado:empleado.salario>50000,ListaEmpleados))
for empleado_salario in salario_altos:
	print(empleado_salario)

#----------------------------------
class Persona:

	def __init__(self, nombre, edad):
		self.nombre=nombre
		self.edad=edad
	def __str__(self):
		return "{} tiene {} años".format(self.nombre,self.edad)

personas=[
Persona("Ana",16),
Persona("Javi es un boomer y",21),
Persona("Aroa",36),
Persona("Salva",6),
Persona("Ricardo",26)
]

personasMayoresEdad=filter(lambda per: per.edad>=18, personas)
for per in personasMayoresEdad:
	print(per)
