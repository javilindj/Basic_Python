'''miDiccionario={"España":"Madrid","Alemania":"Berlin", "Francia":"Paris","Reino Unido":"Londres"}
miDiccionario["Italia"]="Lisboa" # Así añadimos otro clave:valor a un diccionario.
print(miDiccionario)
miDiccionario["Italia"]="Roma" # Al asignar otro valor a la misma clave se sobreescribe, siendo Roma el nuevo valor
print(miDiccionario)
del miDiccionario["Reino Unido"] # Con el parámetro del junto el nombre del diccionario y entre corchetes la clave a eliminar
print(miDiccionario)'''

''' Podemos crear una tupla, damos unos parámetros y con un diccionario diciendole el nombre de la tupla, el número de 
elemento al que pertenece y asignando un valor al imprimirlo nos da el diccionario con sus claves (tuplas)
y los valores que hemos añadido con el diccionario '''

miTupla=("España","Francia","Reino Unido","Alemania")
miDiccionario={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres",miTupla[2]:"Berlin"}
print(miDiccionario)

'''  Aquí mostramos un ejemplo de crear una tupla dentro de un diccionario,
si le decimos que nos muestre el diccionario nos va a mostrar todo el diccionario, si en el print le 
decimos que nos imprima anillos, nos va a imprimir su valor que son los años, si le preguntamos equipo 
no dirá su valor que es Chicago '''

miDiccionario2={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":(91,92,93,96,97,98)}
print(miDiccionario2["anillos"])

''' En el ejemplo de abajo hemos introducido un diccionario dentro del diccionario principal  '''

miDiccionario2={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"Temporadas":(91,92,93,96,97,98)}}
print(miDiccionario.keys()) # Nos devuelve las claves
print(miDiccionario.values()) # Nos devuelve los valores
print(len(miDiccionario2))# Nos dice el número de elementos que componen el diccionario, en este caso 4
print(miDiccionario2)
