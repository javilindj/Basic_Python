
al_cubo=lambda numero:pow(numero,3)

print(al_cubo(13))

multiplica=lambda N1,N2:N1+N2

print(multiplica(5,7))


destatar_valor=lambda comision:"¡{}! €".format(comision)

comision_ana=15000

print(destatar_valor(comision_ana))

saludar = lambda nombre: print(f"Hola {nombre}!!")
saludar("Javi")
saludar("Salva")

maximo = lambda a,b,c: f"El maximo entre {a},{b},{c} es {max(a,b,c)}"

print(maximo(2,7,9))
print(maximo(10,25,92))

def ponerPrefijo(prefijo):
	return lambda nombre: F"{prefijo} {nombre}"

addMr = ponerPrefijo("Mr")
addsr = ponerPrefijo("Sr")
addMis = ponerPrefijo("Miss")

print(addMr("javi"))
print(addsr("Salva"))
print(addMis("Aroa"))

def elevarA(exponente):
	return lambda base: base**exponente

elevarCua= elevarA(2)
elevarCubi= elevarA(3)
print(elevarCua(2))
print(elevarCubi(4))