# entradas: cadena clave
# 	texto a encriptar

# salidas: texto desencriptado



def encriptar():
	textoPlano = open("ejemplo.txt","r")
	textoNuevo = open("textoEncriptado.txt","w")
	clave = input("ingrese una clave: ")
	texto = textoPlano.read()
	alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	tamanoClave = len(clave)
	orden = []

	print(texto)
	for i in range (len(clave)):
		orden.append(alfabeto.find(clave[i]))

	print(orden)

	#ordenamos para tener un orden

	for i in range(1,len (orden)):
		for j in range(0, i):
			if(orden[i] < orden[j]):
				tmp = orden[i]
				orden[i] = orden[j]
				orden[j] =  tmp

	print(orden)

	textoEncriptado = ""
	for i in orden:
		indiceDeClave = clave.find(alfabeto[i])
		print(indiceDeClave)
		indice = indiceDeClave
		while (indice < len(texto)):
			#print("letra agregada",texto[indice])
			textoEncriptado += texto[indice]
			indice += len(clave)
	print(textoEncriptado)

encriptar() 
