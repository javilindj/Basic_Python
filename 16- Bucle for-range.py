'''for i in range(5,50,3): # El tipo range permite notaciones, de esta manera empezaría por el 50, llegaría hasta el 49 e irír de 3 en 3
	print(f"valor de la variable {i}") # la f nos permite concatenar tipo texto con variables.
	'''

valida=False

email=input("Introduce tu email: ")

for i in range(len(email)):

	if email[i]=="@":

		valida=True

if valida:
	print("El email es correcto")

else:
	print("El email es incorrecto")