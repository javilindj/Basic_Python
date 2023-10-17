# Ejercicio 2: 

contra=input("Introduce tu contraseña: ")

contador=0

for i in range(len(contra)):

	if contra[i]==" ":
		contador=1

if len(contra)<8 or contador>0:

	print("contraseña errónea")

else:
	print("contraseña correcta")