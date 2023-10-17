while True:
	nombre = str(input("Introduce tu nombre: "))

	jota = nombre.count("j")
	uve = nombre.count("v")

	if jota==1 and uve==1:
			print("Tu nombre es realmente:", nombre,"alias el Makineitor","\nEl programa ha finalizado")
			break;
	else: 
			print("Mal introducido, intentalo de nuevo")