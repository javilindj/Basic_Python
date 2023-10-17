#Aplica una función a cada elemento de una lista iterable devolviendo otra lista.
#Map pide 2 argumentos  map(funcion,iterable)
import math
eje_x = [0,1,2,3,4,5,6,7,8,9,10]
eje_xx = [3,4,5,6,7,8,9,10,11,12,13]
eje_y = list(map(lambda x,y: round(math.cos(x) + math.exp(y),2),eje_x,eje_xx))
print(eje_y)


#--------------------- Práctica Dimas-------------------
palabras = ("Dale","un","buen","like","y","suscríbete")

longitudes = tuple(map(lambda palabra:len(palabra),palabras))
print("Las longitudes de las palabras son las siguientes:",longitudes)

#---------------------- Práctica Peruvian-----------------
def elevarCuadrado(num):
	return pow(num,2)

numeros = list(range(1,11))
print(numeros)

numerosElevados = list(map(elevarCuadrado,numeros))
print(numerosElevados)

#------------------------ Ejemplo Juan Píldoras informáticas-----
"""class Empleado:

	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario


	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)

ListaEmpleados=[
Empleado("Juan","Director",6700),
Empleado("Ana","Presidenta",7500),
Empleado("Antonio","Administrativo",2100),
Empleado("Sara","Secretaria",2150),
Empleado("Mario","Botones",1800)
]

def calculo_comision(empleado):
	if(empleado.salario<=3000):
		empleado.salario=empleado.salario*1.03

	return empleado
Listaemleadoscomision=map(calculo_comision,ListaEmpleados)

for empleado in Listaemleadoscomision:
	print(empleado)"""