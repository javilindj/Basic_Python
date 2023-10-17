contador=0

miEmail=input("Introduce tu dirección de email: ")

for i in miEmail:
	if(i=="@" or i=="."):
		contador=contador+1

if contador==2:
	print("El email es correcto")
else:
	print("El email es incorrecto")