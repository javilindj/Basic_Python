# Obtener una lista de números pares con una función.
'''def generaPares(limite):
	num=1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num+=1
	return miLista
print(generaPares(10))'''


# Obtener números pares con un generador.
def generaPares(limite):
	num=1
	
	while num<limite:
		yield num*2
		num+=1
devuelvePares=generaPares(60)

#for i in devuelvePares:
	#print(i)

print(next(devuelvePares))

print("aquí")

print(next(devuelvePares))

print("aquí")

print(next(devuelvePares))




