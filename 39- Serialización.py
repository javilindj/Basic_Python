import pickle

lista_nombres = ["Javi", "Aroa", "Salva","Mini Javi"]

fichero_binario = open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

