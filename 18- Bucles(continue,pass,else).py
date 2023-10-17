# Instrucción continue:

'''for letra in "python":
	if letra=="h":
		continue # la intrucción continue hace que el bucle salte la impresión cuando encuentre la letra h
	print("Viendo la letra: " + letra)

nombre="Píldoras Informáticas"

contador=0

for i in nombre: 
	if i==" ": #Aquí mediane un if le decimos que si encuentra un espacio en blanco, omita ese caracter con la instrucción continue
		continue # y sigue el bucle recorriendo el string, nos dice que hay 20 caracteres al omitir el espacio.
	contador+=1 # El operador += incrementa en 1 a cada vuelta de bucle.

print(contador)'''

#Instrucción pass:

'''while True:
	pass '''# Para implementar más tarde, la dejamos creada y con el pass para que no nos genere una excepción

# Instrucción else:

email=input("Introduce email: ")

for i in email:

	if i=="@":
		arroba=True

		break;

else:            # else dentro de un bucle nos lo mostrará si la condición no se cumple sin necesidad de un if, en este caso,
	arroba=False # si introducimos una dirección con @ nos dirá True porque entra dentro del bucle for, 
                 # si la intrudicimos sin ella saltará al else y nos dirá False
print(arroba)