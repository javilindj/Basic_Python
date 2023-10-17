#--------Tipos de datos simples----------https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
#nombre = input("Introduce tu nombre: ")
#print(f"¡Hola",nombre,"!")
"""
horas = float(input("Introduce las horas trabajadas: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Te pertenece cobrar: " + str(paga) + "€")"""

"""peso = float(input("Introduce tu peso: "))
print(peso,"Kg")
estatura = float(input("Introduce tu estatura: "))
print(estatura,"M")
imc = round(float(peso)/float(estatura)**2,3)
print(f"Tu imc es:", imc)"""

"""barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")"""

"""nombre = input("Introduce tu nombre: ")
num = int(input("Introduce el número de veces que quieras que se imprima: "))
print((nombre + "\n") * int(num))"""

"""nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
print((nombre.lower() + "\n") * 3 + (apellido.lower() + "\n") * 3)
print(nombre.upper() + " " + apellido.upper())
print(nombre.capitalize() + " " + apellido.capitalize())


#---------Cadenas-------https://aprendeconalf.es/docencia/python/ejercicios/cadenas/"""

"""nombre = input("Introduce tu nombre, por favor: ")
print(f"El nombre {nombre.upper()} tiene {len(nombre)} letras")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")"""

"""telf = input("Introduce el número de teléfono en formato +xx-xxxxxxxxx-xx: ")
print("El número de teléfono es ",telf[4:-3]) # accedemos al índice 4 y le decímos que nos  
											  # descuente los 3 últimos caracteres.""" 

"""frase = input("Introduce una frase ")
print(frase[::-1])"""

"""frase = input("Introduce un frase: ")
vocal = input("Introduce una vocal: ")
print(frase.replace(vocal, vocal.upper()))"""

"""email = input("Introduce tu email: ")
print(email[:email.find('@')] + '@ceu.es')"""

"""precio = input("Introduce el precio del producto: ")
print(precio[:precio.find(".")], "euros y ", precio[precio.find(".")+1:], "céntimos.")"""

"""fecha = input("Introduce tu fecha de nacimiento: ")
print("Día",fecha[0:2])
print("Mes",fecha[3:5])
print("Año",fecha[6:])

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)"""

"""lista_compra = input("Introduce tu lista de la compra: ")
print(lista_compra.replace(",","\n"))"""

"""nombre_producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))
total = precio * unidades
print('{nombre_producto}:{unidades} unidades x {precio:.2f} € = {total:.2f} €'.format(nombre_producto = nombre_producto, unidades = unidades, precio = precio, total = total))"""
# Info sobre format() en: https://docs.python.org/es/3/tutorial/inputoutput.html

"""puesto = input("Introduce tu puesto de trabajo: ")
horas = float(input("¿Cuantas horas tienes este mes?: "))
precio = float(input("¿Cuanto es el precio por hora?: "))
total = horas * precio
print('Tu puesto de trabajo es: {puesto}, has echado {horas:.3f} horas de trabajo, cada hora tiene un precio de {precio:.3f}€ y suman un total de {total:4f}€'.format(puesto=puesto,horas=horas,precio=precio,total=total))"""

#-----Condicionales------- https://aprendeconalf.es/docencia/python/ejercicios/condicionales/

"""edad = int(input("Introduce tu edad, por favor: "))
if edad >= 18:
	print("Eres mayor de edad")
else:
	print("Eres menor de edad")"""

"""string = "contraseña"
intr_contra = input("Introduce tu contraseña: ")
if intr_contra.lower() == string:
	print("La contraseña coincide")
else:
	print("La contraseña no coincide")"""

"""n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
if n1/n2 == 0:
	print("¡Error!, no se puede dividir entre 0")
else:
	print("El resultado de la división es: ",n1/n2)"""

"""num = int(input("Introduce un número al azar: "))
if num % 2 == 0:
	print("El número", num, "es par")
else:
	print("El número", num, "es impar")"""

"""edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos: "))
if edad >=16 and ingresos >=1000:
	print("Tienes que tributar")
else:
	print("No tienes que tributar")""" 

"""nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M o F): ")

if nombre.lower() < "m" and sexo.lower() == "f":
	print("Perteneces al grupo A")
elif nombre.lower() > "n" and sexo.lower() == "m":
	print("Perteneces al grupo B")
else:
	print("Ve a First Dates")"""

"""renta = float(input("Introduce tu renta anual: "))
if renta < 10000:
	tipo = 5
elif renta < 20000:
	tipo = 15
elif renta < 35000:
	tipo = 20
elif renta < 60000:
	tipo = 35
else:
	tipo = 45
print(f"El tipo de interés es del: ",tipo,"%" " y el importe a pagar sería: ", tipo * renta / 100,"€")"""

"""extra = 2400
nivel = float(input("Introduce el nivel de rendimiento: "))
if nivel == 0.0:
	extra = 0
	nivel = "Inaceptable"
elif nivel == 0.4:
	extra = nivel * extra
	nivel = "Aceptable"
elif nivel >= 0.6:
	extra = nivel * extra
	nivel = "Meritorio"
print(f"El nivel del trabajador es: ",nivel,"\nTiene una paga de beneficios de: ",extra,"€")"""

"""edad = int(input("Introduce tu edad, por favor: "))
if edad < 4:
	entrada = "Gratis"
elif edad <= 18:
	entrada = 5
else:
	entrada = 10
print('Tienes {edad} años y el precio de la entrada son {entrada} €'.format(edad=edad,entrada=entrada))"""

"""print("Bienvenido a la pizzería Bella Napoli\n1 - Pizza Vegetariana \n2 - Pizza No Vegetariana")
pedido = int(input("Introduce el tipo de pizza que deseas: "))
if pedido == 1:
	ingredientes = int(input("Introduce el ingrediente: \n1 - Tofu \n2 - Pimiento: "))
	if ingredientes == 1:
		ingredientes = "Tofu"
	else:
		ingredientes = "Pimiento"
	print("Pizza Vegetariana con Mozzarella, Tomate y ", ingredientes)
else:
	ingredientes = int(input("Introduce el ingrediente: \n1 - Peperoni \n2 - Jamón \n3 - Salmón "))
	if ingredientes == 1:
		ingredientes = "Peperoni"
	elif ingredientes == 2:
		ingredientes = "Jamón"

	else:
		ingredientes = "Salmón"
	print("Pizza no Vegetariana con Mozzarella, Tomate y ",ingredientes)"""

#---------- Bucles ---------- https://aprendeconalf.es/docencia/python/ejercicios/bucles/

"""cadena = input("Escribe una palabra: ")
for i in range(10):
	print(cadena)"""

"""edad = int(input("Introduce tu edad: "))
for i in range(edad):
	print("Has cumplido ", i +1, " años")"""

"""num = int(input("Introduce un número entero: "))
for i in range(1,num,2):
	print(i, end=",")"""

"""num = int(input("Introduce un número para iniciar la cuenta atrás: "))
for i in range(num,-1,-1):
	print(i, end=",")"""

"""cantidad = float(input("Introduce la cantidad: "))
interes = float(input("Introduce el interés: "))
anos = int(input("Introduce el número de años: "))
for i in range(anos):
	cantidad *= 1 + interes/100
	print("El interés acumulado tras " + str(i+1) + " años " + str(round(cantidad,2)))"""	

"""num = int(input("Introduce un número entero: "))
for i in range(num):
	for j in range(i+1):
		print("*", end="")
	print("")"""
"""for i in range(1,11):
	for j in range(1,11):
		print(i*j,end="\t")
	print("")"""

"""n = int(input("Introduce un número entero para un triángulo - rectángulo: "))
for i in range(1,n+1,2):
	for j in range(i,0,-2):
		print(j,end="")
	print("")"""

"""key = "contraseña"
password = input("Introduce la contraseña: ")
while password != key:
	print("contraseña mal introducida, prueba de nuevo")
	password = input("Introduce la contraseña: ")
print("La contraseña  ********** es correcta")"""

"""palabra = input("Introduce una palabra: ")
for i in range(len(palabra)-1,-1,-1):
	print("la palabra en cuestión es: ",palabra[i])"""

"""frase = input("Introduce una frase: ")
letra = input("Introduce la letra: ")
contador = 0
for i in frase:
	if i == letra:
		contador += 1
print("La letra --{letra}-- aparece {contador} veces y la frase es: {frase}".format(letra=letra,contador=contador,frase=frase))"""

"""while True:
	frase = input("Introduce algo: ")
	if frase == "salir":
		break
	print(frase)"""

# -------- Listas y tuplas --------- https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

"""asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
print(asignaturas)"""

"""asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
for i in asignaturas:
	print("Yo estudio", i)"""

"""asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
notas = []
for i in asignaturas:
	nota = input("¿Qué nota has sacado en " + i + "? ")
	notas.append(nota)
for i in range(len(asignaturas)):
	print("En " + asignaturas[i] + " has sacado un " + notas[i])"""

"""ganadores =[]
for i in range(6):
	ganadores.append(int(input("Introduce el número ganador: ")))
ganadores.sort()
print("Los números ganadores son: " + str(ganadores))"""

"""num = [1,2,3,4,5,6,7,8,9,10]
num.reverse()
print(num,end=",")"""

"""num = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
	print(num[-i], end=",")"""

"""suspensa = []
asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
for i in asignaturas:
	nota = int(input("Introduce la nota en " + i + " :"))
	if nota < 5:
		suspensa += [i]
print(f"Las asignaturas a repetir son: ", suspensa)"""

"""abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m"
,"n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(abecedario),1,-1):
	if i % 3 == 0:
		abecedario.pop(i-1)
print(abecedario)"""

"""palabra = input("Introduce una palabra: ")
reves = palabra
palabra = list(palabra)
reves = list(reves)
reves.reverse()
if palabra == reves:
	print("Es un palíndromo")
else:
	print("No es un palíndromo")"""	

"""palabra = input("Introduce una palabra: ")
vocales = ["a","e","i","o","u"]
for vocal in vocales:
	veces = 0 
	for letras in palabra:
		if letras == vocal:
			veces += 1
	print("La vocal " + vocal + " aparece " +  str(veces) + " veces")"""

"""precios = [50,75,46,22,80,65,8]
min = max = precios[0]
for precio in precios:
	if precio < min:
		min = precio
	elif precio > max:
		max = precio
print("El mínimo es ", min)
print("El máximo es ", max)"""

"""precio = [3,33,21,1,2,9,75]
min = max = precio[0]
for p in precio:
	if p < min:
		min = p
	elif p > max:
		max = p
		
print("El precio mínimo es: ", min)
print("El precio máxiomo es: ", max)"""

"""a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) """

# ------- Diccionarios ---------- https://aprendeconalf.es/docencia/python/ejercicios/diccionarios/

"""divisas = {"Euro":"€", "Dolar":"$", "Yen":"&"}
moneda = input("Introduce una divisa: ")
print(divisas.get(moneda.title(),"La divisa no está."))"""

"""nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu dirección: ")
telefono = int(input("Introduce tu teléfono: "))
datos = {"nombre": nombre, "edad":edad, "direccion": direccion, "telefono":telefono}
print(datos['nombre'], 'tiene ', datos['edad'], 'años, vive en ',datos['direccion'],'y su teléfono es ' ,datos['telefono'])"""

"""frutas = {'platano':1.35, 'manzana':0.80, 'pera':0.85, 'naranja':0.70}
fruta = input("Elija una fruta: ")
kg = float(input("Introduzca la cantidad en kg: "))
if fruta in frutas:
	print(kg,'Kilos de', fruta, 'valen', frutas[fruta]*kg,'€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")"""

"""meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])"""

"""curso = {'Matemáticas':6, 'Física':4, 'Química':5}
total_creditos = 0
for asignatura, creditos in curso.items():
	print(asignatura, 'tiene', creditos, 'créditos')
	total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)"""

"""yo = {}
continuar = True
while continuar:
	clave = input("¿Qué dato quieres añadir?: ")
	valor = input(clave + ": ")
	yo[valor] = clave
	print(yo)
	continuar = input("¿Quieres añadir algún dato más?: ")
	if continuar == "si":
		print("ok boomer")
	else:
		print("el programa ha finalizado")
		break;"""

"""cesta = {}
continuar = True
while continuar:
	clave = input("Introduce un artículo: ")
	valor = float(input("Introduce el precio de " + clave + ": "))
	cesta[clave] = valor
	continuar = input("¿Deseas añadir algo más a la cesta?: ") =="si"
precio = 0
print('Lista de la compra')
for clave, valor in cesta.items():
	print(clave, '\t', valor, "€")
	precio += valor
print('Precio total: ', precio)"""

"""diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')"""

"""facturas = {}
cobrado = 0 
pendiente = 0
more = ''
while more != 'T':
	if more == 'A':
		clave = input('Introduce el número de factura: ')
		coste = float(input('Introduce el coste de la factura: '))
		facturas[clave] = coste
		pendiente += coste
	if more == 'P':
		clave = input('Introduce el número de factura a pagar: ')
		coste = facturas.pop(clave,0)
		cobrado += coste
		pendiente -= coste
	print('Recaudado', cobrado)
	print('Pendiente de cobro: ', pendiente)
	more = input('¿Quieres añadira una nueva factura (A), pagarla (P) o terminar (T): ').upper()"""

"""bbdd = {}
preferentes = {}
continuar = True
while continuar:
	continuar = input('¿Qué desea hacer? \n(1) Añadir cliente \n(2) Eliminar cliente \n(3) Mostrar cliente \n(4) Listar todos los clientes, \n(5) Listar clientes preferentes \n(6) Terminar \nInserta una de las 6 opciones: ')
	if continuar == "1":
		clavenif = input("Introduce el nif: ")
		valornif = input("Introduce los datos pertenecientes al nif " + clavenif + ": ")
		preferente = input('¿Es un cliente preferente?: \ns: \nn:\n ')
		if preferente == "s":
			preferentes[clavenif] = valornif
			
		else:
			bbdd[clavenif] = valornif
			
	elif continuar == "2":
		clavebor = input('Introduzca el NIF que desea eliminar: ')
		if clavebor == clavenif:
			borrar = bbdd.pop(clavebor,0)
			print('Registro borrado correctamente')
		else:
			print('El cif introducido no existe')
			clavebor = input('Introduzca el NIF que desea eliminar: ')
	elif continuar == "3":
		clave_ver = input('Introduce el NIF del cliente a consultar: ')
		if clave_ver == clavenif:
			print(valornif)
	elif continuar == '4':
		print(bbdd, preferentes)
	elif continuar == '5':
		print(preferentes)
	else:
		print('El progarama ha finalizado')
		break;"""
"""clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if opcion == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')"""

"""clientes = {}
opcion = ''

while opcion != '6':
	if opcion == '1':
		nif = input('Introduce tu nif: ')
		nombre = input('Introduce tu nombre: ')
		direccion = input('Introduce tu direccion: ')
		telefono = input('Introduce tu telefono: ')
		vip = input('¿Es un cliente VIP? (s/n)')
		cliente = {'nombre':nombre, 'direccion':direccion, 'telefono':telefono, 'preferente':vip=='s'}
		clientes[nif] = cliente
	if opcion == '2':
		borrar = input('Introduce el nif a borrar: ')
		if borrar == nif:
			del nif
	if opcion == '3':
		nif = input('Introduce el nif a visualizar: ')
		if nif in clientes:
			print('NIF:', nif)
			for clave, valor in clientes[nif].items():
				print(clave.title() + ':', valor)

	if opcion == '4':
		print('Lista de clientes')
		for clave, valor, in clientes.items():
			print(clave,valor['nombre'])
	if opcion == '5':
		print('Lista de clientes Vip')
		for clave, valor in clientes.items():
			if valor['preferente']:
				print(clave, valor['nombre'])
	opcion = input('Menu de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar \nElija una opción: ')"""

"""
# Cadena con los datos de los clientes de la empresa
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# Dividimos la cadena por el caracter de cambio de línea \n y creamos una lista con las subcadenas
lista_clientes = datos_clientes.split('\n')
# Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
directorio = {}
# Dividimos la cadena del primer elemento de la lista de clientes (que contienen los 
# nombres de los campos) por el caracter ; y creamos una lista con los campos.
lista_campos = lista_clientes[0].split(';') 
# Bucle iterativo para recorrer los elementos de la lista lista_clientes.
# la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista 
# (el primer elemento contiene los nombres de campo así que no corresponde a un cliente)
for i in lista_clientes[1:]:
    # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
    cliente = {}
    # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
    # información del cliente
    lista_info = i.split(';') 
    # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
    # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde 
    # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
    # principal
    for j in range(1,len(lista_campos)):
        # Condicional. Si el campo actual es descuento convertimos su valor en real
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    # Añadirmos un par al diccionario del directorio con la clave el nif del cliente y valor
    # el diccionario que acabamos de crear con el resto de sus datos.
    directorio[lista_info[0]] = cliente
# Mostramos el diccionario por pantalla
print(directorio)"""

# --------- Funciones ------ https://aprendeconalf.es/docencia/python/ejercicios/funciones/

"""def saludo():
	print('¡Hola amiga!')
saludo()"""

"""def saludo(nombre):
	print('¡Hola',nombre,'!')
saludo('javi')"""

"""def factorial(n):
	tmp = 1 
	for i in range(n):
		tmp *= i+1
	return tmp
print(factorial(4))
print(factorial(20))"""

"""def factura(precio,iva=21):
	return precio + precio*iva/100
print(factura(1000,10))
print(factura(1000))"""

"""def circulo(radio):
	pi = 3.1415
	return pi*radio**2

def cilindro(radio, altura):
	return circulo(radio)*altura

print(cilindro(3,5))"""

"""def calc_media(ejemplo):
	return sum(ejemplo)/len(ejemplo)
print(calc_media([100,200]))"""

"""def num_cuadrado(ejemplo):
	lista = []
	for i in ejemplo:
		lista.append(i**2)
	return lista

print(num_cuadrado([2,4,5]))"""

"""def square(sample):
    #Función que calcula los cuadrados de una lista de números.
    #Parámetros
    #sample: Es una lista de números
    #Devuelve una lista con los cuadrados de los números de la lista sample.
    
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    #Función que calcula la media, varianza y desviación típica de una muestra de números.
    #Parámetros
    #sample: Es una lista de números
    #Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))"""

"""def mcd(n, m):
    Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))"""

"""def to_decimal(n):
    Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))"""

"""def contar_palabras(texto):
    #Función que cuenta el número de veces que aparece cada palabra en un texto.
    #Parámetros:
    #    - text: Es una cadena de caracteres.
    #Devuelve: 
     #   Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def mas_repetidas(palabras):
    max_palabra = ''
    max_frecuente = 0
    for palabra, frecuente in palabras.items():
        if frecuente > max_frecuente:
            max_palabra = palabra
            max_frecuente = frecuente
    return max_palabra, max_frecuente

texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(contar_palabras(texto))
print(mas_repetidas(contar_palabras(texto)))"""

# -------- Programación funcional -------- https://aprendeconalf.es/docencia/python/ejercicios/programacion-funcional/

"""def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n * n

print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))"""

"""def aplica_funcion(funcion,lista):
	
	l = []
	for i in lista:
		if funcion(i):
			l.append(i)
	return l
def par(n):
	return n % 2 == 0

print(aplica_funcion(par,[1,2,3,4,5,6]))"""

"""def longitud_palabras(frase):
	palabras = frase.split()
	longitud = map(len,palabras)
	return dict(zip(palabras,longitud))
print(longitud_palabras('Bienvenidos a Python'))"""

"""def longitud_palabra(frase):
   
    return {palabra:len(palabra) for palabra in frase.split()}

print(longitud_palabra('Bienvenidos a Python'))"""

"""def calificaciones(nota):
	if nota < 5:
		return 'Suspenso'
	elif nota < 7:
		return 'Bien'
	elif nota < 9:
		return 'Notable'
	elif nota < 10:
		return 'Sobresaliente'
	else:
		return 'Matrícula de honor'
def aplicar_calificaciones(notas):
	return list(map(calificaciones,notas))
print(aplicar_calificaciones([6.5,5,3.4,8.2,2.1,9.7,10]))"""

"""def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def passed_subject(subject):
    '''
    Función que recibe una tupla con una asignatura y su nota y devuelve True si la asignatura está aprobada o False si está suspensa.abs
    Parámetros:
        subject: Es una tupla (asignatura, nota) donde nota es un valor real entre 0 y 10.
    Devuelve: True si la nota es mayor o igual que 5 y False si no.abs
    '''
    return (subject[1] >= 5)


def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    passed = dict(filter(passed_subject, scores.items()))
    subjects = map(str.upper, passed.keys())
    grades = map(grade, passed.values())
    return dict(zip(subjects, grades))

print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))"""

# Escribe una función que calcule el módulo de un vector:

"""def sum_square(x,y):
	return x + y **2 # función que calcula un numero mas el otro al cuadrado

def module(v):
	from functools import reduce
	return reduce(sum_square,v,0)** 0.5 # v es un tupla, función que calcula el módulo de un vector

print(module((3,4)))
print(module((1,2,3)))"""


"""pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def añadir_precio(piso):
	precio = (piso['metros'] * 1000 + piso ['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año'])/100)
	if piso['zona'] == 'B':
		precio *=1.5000
	piso['precio'] = precio
	return piso

def busca_piso(pisos, presupuesto):
	def filtro(piso):
		return piso['precio'] <= presupuesto

	return list(filter(filtro,map(añadir_precio,pisos)))
print(busca_piso(pisos,100000))"""


"""from statistics import mean, stdev

def atipico(muestra):
    media = mean(muestra)
    desviacion = stdev(muestra)
    def f(n):
        puntuacion = (n - media) / desviacion
        return (puntuacion < -3) or (puntuacion > 3)
    return f

def datos_atipicos(muestra):
    return list(filter(atipico(muestra), muestra))

print(datos_atipicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))"""

"""email = input('Introduce tu email: ')
while email:
	if email.count('@') != 0 and email.count('.') != 0:
		print(f'Email introducido es: ' + email)
		break;
	else:
		print('Email erroneo, vuelva a introducirlo: ')
		email = input('Introduce tu email:')
		print('Solo un mongólico pone así el email')

print('El programa de reconocimiento de email ha finalizado')"""

"""n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
f = open(nombre_fichero, 'w')
for i in range(1,11):
	f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()"""

"""n = int(input('Introduce el número que quieras entre el 1 y el 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try:
	f = open(nombre_fichero, 'r')
except FileNotFoundError:
	print('No existe el fichero con la tabla del ', n)
else:
	print(f.read())
	f.close()"""

"""n = int(input('Introduce un número del 1 al 10: '))
nf = 'Tabla ' + str(n) + '.txt'
f = open(nf, 'w')
f.write('A continuación vamos a mostrar la tabla del ' + str(n) + '\n')
for i in range(1,11):
	f.write(str(n) + ' por ' + str(i) + ' es igual a ' + str(n * i) + '\n')
f.write('Así finaliza la tabla del ' + str(n))
f.close()"""

n = int(input('Introduce un número entre el 1 y 10: '))
m = int(input('Introduce otro número entre el 1 y 10: '))
nf = 'tabla-n' + str(n) + '.txt'
try:
	f = open(nf, 'r')
except FileNotFoundError:
	print('No existe la tabla del ' + str(n))

else:
	for i in range(1,11):
		f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * m) + '\n') 

f.close()