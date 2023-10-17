# Ejercicio 3: Crea un programa que pida un email que tenga una @ y un punto al menos, si tiene ambas cosas ok, sino error

email=input("Introduce tu email: ")

contaPun=0
contaArro=0

for i in range(len(email)):
	
	if email[i]=="@":
		contaArro=contaArro+1


	if email[i]==".":
		contaPun=contaPun+1

if contaPun==0 or contaArro!=1:
	
	print("email incorrecto")

else: 
	print("Email correcto")