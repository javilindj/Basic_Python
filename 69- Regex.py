import re

cadena= "Vamos a aprender expresiones regulares en Python. Python es bien"
textoBuscar="aprender"
textoEncontrado=re.search(textoBuscar,cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())
textoBuscar="Python"
print(len(re.findall(textoBuscar,cadena)))
if re.search(textoBuscar,cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")
