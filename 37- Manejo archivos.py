from io import open

#--------Creación y apertura de archivo

'''archivo_texto=open("archivo.txt","w")

frase="Estupendo día para estudiar python\n el miércoles"

archivo_texto.write(frase)

archivo_texto.close()'''

#---------Leer un archivo
Archivo_texto=open("archivo.txt","r")

#texto=archivo_texto.read()
lineas_lista=Archivo_texto.readlines()

Archivo_texto.close()

print(lineas_lista[1])


#--------Añadir texto
'''
archivo_texto=open("archivo.txt","a")
archivo_texto.write("\n siempre es una buena ocasión para estudiar python")
archivo_texto.close()'''



