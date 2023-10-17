import re
# Metacaracter ^ es para que empiece por esa palabra.
# Metacaracter $ es para que finalice por esa palabra.
# Palabra entre corchetes es para buscar una palabra o carácter en 
# concreto que tenga lo que introducimos en el corchete.
lista_nombres = ["Ana Gómez",
					"Maria Martín",
					"Sandra López",
					"Santiago Martín",
					"Sandra Fernandez"]
for elemento in lista_nombres:
	if re.findall("^Sandra",elemento):

		print(elemento)

for elemento in lista_nombres:
	if re.findall("Martín$",elemento):

		print(elemento)

lista_direcciones = ["http://pildorasinformaticas.es",
 					"http://pildorasinformaticas.com",
 					"ftp://pildorasinformaticas.es",
 					"ftp://pildorasinformaticas.es",
 					"ftp://pildorasespañolas.arg"]

for elemento in lista_direcciones:
	if re.findall("[ñ]",elemento):  

		print(elemento)

lista_cosas=("Tarjeta gráfica",
				"Móvil",
				"Monitor",
				"Pulsómetro")
for elemento in lista_cosas:
	if re.findall("[óá]",elemento):
		print("Lleva tilde:",elemento)