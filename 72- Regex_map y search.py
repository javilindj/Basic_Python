import re
#re.match(x,y) busca solo al principio
nom1="sara López"
nom2="Antionio Gómez"
nom3="mara López"
if re.match("Sara", nom1,re.I):# re.I es para eliminar el case sensitive
#if re.match(".ara",nom2):
	print("Hemos encontrado el nombre")

else: 
	print("No hemos encontrado el nombre")

cadena1="Jara López"
cadena2="544545454"
cadena3="a54545454"

if re.match("\d",cadena3):#"\d" sirve para preguntar si empieza por un dígito.
	print("Hemos encontrado el número")
else:
	print("No hemos encontrado el número")
#re.search(x,x) Busca en todo el texto.

nom1="Aroa López"
nom2="Javi Gallego"
nom3="Jose López"

if re.search("López",nom2):
	print("Lo hemos encontrado search")
else:
	print("No lo hemos encontrado search")

codigo1="dfksgjdklsfjgkls71djfglkjskljgdsklj"
codigo2="jfjdakljf71jdsklfja klsdajflakjsdfkl lajdf"
codigo3="jkfkasdj kldsfjll adfkljasdkl ksdjf"

if re.search("71",codigo3):
	print("71 encontrado")
else:
	print("71 no encontrado")

	#Buscar patrones busqueda python en google