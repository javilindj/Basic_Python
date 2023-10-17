print("Selección de asignaturas optativas")

print("Asignaturas optativas: Informática - Software - Accesibilidad")

opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower() # aquí lo que decimos que si escribimos con mayúsculas y minúsculas solo lo acepte como minúsculas

if asignatura in ("informática", "software", "accesibilidad"): 
	print("La asignatura escogida es: " + asignatura)

else:
	print("La asignatura escogida no está")

''' in busca dentro de la variable si está el str o int, pyhton al ser case diferencia entre
mayúsculas y minúsculas podemos usar lower(minusculas), upper(mayúsculas) '''