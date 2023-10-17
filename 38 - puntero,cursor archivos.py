from io import open

archivo_texto=open("archivo.txt","r+") # con r+ le decimos que es de lectura y escritura
archivo_texto.write("ComienxANDO CURSO")

#archivo_texto.seek(len(archivo_texto.read())/2) # De este modo nos posiciona en la mitad del texto.
#archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.readlines())
#archivo_texto.seek(11) # seek() indica la posición del puntero/cursor

#print(archivo_texto.read(11))

#print(archivo_texto.read())
