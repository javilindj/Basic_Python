nu1=int(input("Introduce un numero: "))
nu2=int(input("Introduce otro numero: "))

def DevuelveMax(n1,n2):

	if n1<n2:
		print(n2)

	elif n2>n1:
		print(n1)

	else:
		print("Ninguno, son iguales")

print("El número más alto es: ")

DevuelveMax(nu1,nu2)

