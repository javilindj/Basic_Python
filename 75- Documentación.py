"""Incluir comentarios en clases, métodos y módulos
Sirve para el trabajo en equipo o simplemente para tener documentado alguna práctica o módulo
por si queremos rehusarlo en el futuro"""
class Areas:
	"""Esta clase calcula las áreas de diferentes figuras geométricas"""

	def areaCuadrado(lado):
		"""Calcula el área del cuadrado
		elevando al cuadrado el lado pasado
		por parámetro"""
		return "El área del cuadrado es: " +str(lado*lado)

	def areaTriangulo(base,altura):
		"""Calcula el área del triángulo
		utilizando los parámetros base * altura"""
		return "El área del triángulo es: " +str((base*altura)/2)

#print(areaCuadrado(5))

help(Areas) # Con help nos imprime directamente la documentación que hay dentro de esa función.
						 # Si la función está dentro de una clase debemos poner clase.funcion
#print(areaTriangulo(5,2))