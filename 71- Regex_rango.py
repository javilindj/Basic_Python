import re 
lista_nombres = ["Javi",
				"Aroa",
				"Salva",
				"Pedro",
				"Miriam"]


for elemento in lista_nombres:
	if re.findall("[A-L]", elemento):

		print(elemento)

lista_móviles = ("Pixel 6",
				"Pixel7",
				"Pixel7a",
				"Pixel 5",
				"Pixel 6a",
				"Pixel 4Xl")

for elemento in lista_móviles:
	if re.findall("Pixel[^4-6]",elemento): # Dentro del rango si ponemos delante ^ nos 
		print(elemento)                    # devuelve lo contrario, lo negado.

lista_ciudad = ["Ma1",
				"Ba1",
				"Va1",
				"Ma2",
				"Ba2",
				"Ma3",
				"Ma4",
				"MaA",
				"MaB",
				"MaC"]
for elemento in lista_ciudad:
	if re.findall("Ma[1-4A-B]", elemento):
		print(elemento)