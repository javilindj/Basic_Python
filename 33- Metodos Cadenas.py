mail = str(input("Introduce tu correo: ->"))

arroba = mail.count("@")
punto = mail.count(".")


while mail:

	if arroba!=1 or punto!=1 or mail.startswith('@') or mail.endswith('@'):
		print("Mail incorrecto, vuelve a intentarlo ->")
		mail = input("Introduce tu correo: ->")

	else:
		print("El email introducido:", mail, "es correcto,\nEl programa ha finalizado")
		break;
		
'''
upper() sube todo en mayúsculas
lower() baja todo en minúscula
capitalize() todas la primera letra en mayúscula
count() contar una y cuantas aparecen dentro de una cadena
find() representa el índice donde aparece un carácter dentro de un texto
isdigit() devuelve un booleano si es un valor numérico o no
isalum() comprueba si es alfanuméricos
isalpha si es alpha comprueba si son solo letras
split()  separa por palabras utilizando espacios
strip() borra los espacios sobrante al principio y al final
replace() cambia una palabra o una letra por otra
rfind() representa el índice de un carácter contando desde atrás'''