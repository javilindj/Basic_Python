def devuelveCiudades(*ciudades):# El asterisco nos permite poner un número indeterminado de parámetros mediante una tupla a esa función.
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento # yield from nos permite hacer un yield desde el primer elemento, asi no tenemos que usar sublementos en bucles anidados


ciudades_devueltas=devuelveCiudades("Madrid","Barcelona","Murcia","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))