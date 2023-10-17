print("Programa de Becas 2023")

distancia=int(input("Introduzca la distancia al centro: "))
print("Distancia: " + str(distancia) + "KMS") # Concatenación de de str con int separados por símb +
hermanos=int(input("Introduzca el número de hermanos: "))
print("Hermanos: " + str(hermanos))
salario=int(input("Introduzca el salario: "))
print("Salario: " + str(salario) + "€")

if distancia>40 and hermanos>2 or salario<=20000: # Condicionales and (y si además), or (o si no)
	print("Tienes derecho a beca")

else:
	print("No tienes derecho a beca")