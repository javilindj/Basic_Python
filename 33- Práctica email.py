while True:

	mail = str(input("Introduce tu email: "))

	arroba = mail.count("@")

	punto = mail.count(".")

	arroba_principio = mail.startswith("@")

	arroba_final = mail.endswith("@")



	if arroba!=1 or punto!=1 or arroba_principio or arroba_final:
			print("Email incorrecto")
			

	else:
			print("Email", mail, "es correcto.\nEl programa ha finalizado")
			break;