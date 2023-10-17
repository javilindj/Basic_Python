def areaTriangulo(base,altura):

	
	"""
	Calcula al área de un triángulo dado
	>>> areaTriangulo(3,6)
	'El área del triángulo es: 9.0'
	
	>>> areaTriangulo(4,5)
	'El área del triángulo es: 10.0'

	>>> areaTriangulo(9,3)
	'El área del triángulo es: 13.5'

	"""
	return "El área del triángulo es: " +str((base*altura)/2)

def compruebaMail(mailUsuario):
	"""
	la función compruebaMail evalúa un mail
	recibido en busca de la @. Si tiene una @
	es correcto, si tiene más de una @ es incorrecto
	si la @ está al final es incorrecto

	>>> compruebaMail('javi@msn.com')
	True

	>>> compruebaMail('javimsn.com@')
	False
	
	>>> compruebaMail('javi@msn.@com')
	False

	>>> compruebaMail('javimsn.com')
	False


	"""
	arroba=mailUsuario.count('@')
	if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1)or mailUsuario.find('@')==0):
		return False
	else:
		return True

mailUsuario=input("Introduce tu email, por favor: ")
#import doctest
#doctest.testmod()