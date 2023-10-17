print("Salarios empresa")

salario_presidente=int(input("Introduce el salario del Presidente: "))
print("Salario Presidente: " + str (salario_presidente)) # Para  concatenar strings e int tenemos que poner str(nombre variable)
salario_director=int(input("Introduce el salario del Director: "))
print("Salario Director: " + str (salario_director))
salario_contable=int(input("Introduce el salario del Contable: "))
print("Salario Contable: " + str (salario_contable))
salario_administrativo=int(input("Introduce el salario del Administrativo: "))
print("Salario Administrativo: " + str (salario_administrativo))

if salario_presidente>salario_director>salario_contable>salario_administrativo:
	print("Todo funciona correctamente")

else:
	print("Algo va mal")