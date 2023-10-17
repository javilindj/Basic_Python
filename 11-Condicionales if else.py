print("Verificación de acceso") # Título que nos muestra al abrir la consola

edad=int(input("Introduce la edad del usuario: ")) # Aquí se detiene la ejecución esperando un valor de tipo entero 

''' El condicional if nos dice que si se cumple esa condición nos imprima el mensaje, sino
se cumple continua el flujo de ejecución, después llega al elif, elif si introduce cuando más de 2 condiciones,
si no cumple el elif lo saltará y pasará al else  '''

if edad<18:
	print("No puedes pasar")

elif edad>100:
		print("Edad incorrecta")

else:
	print("Puedes pasar")

print("El programa ha finalizado")