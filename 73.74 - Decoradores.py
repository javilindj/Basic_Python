#Funciones que añaden funcionalidad a otras funciones.
#Estructura de un decorador: 3 funciones (A,B,C) donde A recibe como parámetro a B para devolver C.
#Un decorador devuelve una función.
def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args,**kwargs): # Con **kwargs 
		#Acciones adicionales que decoran o agregan.
		print("Vamos a realizar un cálculo: ")
		funcion_parametro(*args,**kwargs) # Con *args le decimos que puede recibir un numero indeterminado de parámetro 
		#Acciones adicionales que decoran
		print("Hemos terminado el cálculo")
	return funcion_interior
@funcion_decoradora #Colocando @ junto con el nombre del decorador, nos agrega lo que hemos
def suma(n1,n2,n3):         #agredado en la función decoradora.
	print(n1+n2+n3)
@funcion_decoradora
def resta(n1,n2):
	print(n1-n2)
@funcion_decoradora
def potencia(base,exponente):
	print(pow(base,exponente))
	
suma(7,5,8)
resta(12,10)
