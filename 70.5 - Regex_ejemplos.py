import re

texto = '''Hola Mundo.
Me gusta Python
Mi primer número de la suerte es 987-654-321
Mi segundo número de la suerte es 876-543-210
Mi tercer número de la suerte es 765-432-100
Mi cuarto número de la suerte es 123-456-123-123'''

#print(re.search(r"\d", texto)) # Busca el primer emparejamiento de dígitos. 
#La "r" sirve para anular otras expresiones de Python
print(re.search(r'Mundo.$',texto, flags=re.M)) # re.M agrega un valor de texto a cada línea,re.I ignora case sentitive
print(re.findall(r"\d", texto)) # Busca todos los emparejamientos de dígitos


'''Metacaracteres:
\d      - Digitos (0-9)
\D      - No digitos (0-9)
\w      - Caracter de palabra (a-z, A-Z, 0-9, _)
\W      - No caracter de palabra
\s      - Espacio en blanco (espacio, tab, nueva linea)
\S      - No espacio en blanco (espacio, tab, nueva linea)
.       - Cualquier caracter excepto nueva linea (codicioso - greedy)
\       - Cancela caracteres especiales

^       - Inicio de una cadena de caracteres (string)
$       - Fin de una cadena de caracteres

Cuantificadores:
*       - 0 o más (codicioso - greedy)
+       - 1 o más (codicioso - greedy)
?       - 0 or 1 (perezoso - lazy)
{3}     - Numero exacto
{n,}    - Numero n+
{3,4}   - Rango de números (Minimo, Maximo)
-.+-	- Toma lo que hay entre 2 guiones.
( )     - Grupos
[]      - Encuentra caracteres en corchetes
[^ ]    - Encuentra caracteres que no están dentro de corchetes
|       - Condicional O

\b      - Limite de palabra
\B      - No limite de palabra

\1      - Referencias'''

# Encontrar puntuaciones:

print("Puntuación encontrada",re.findall(r'[^\w\s]',texto))

# Encontrar Fechas:

texto2 = '''
24-11-2014
18-06-2018
03-05-1981
1985-09-04
2018-06-03
'''
print("Las fechas encontradas son: ",re.findall(r'\d{2}-\d{2}-\d{4}',texto2))

# Encontrar usuarios:
# condiciones : 4-14 y solo números o letras
user = '''
javier10
221
abc
javilindj21
'''

print("Los usuarios encontrados son: ",re.findall(r'[a-z0-9]{4,14}',user))