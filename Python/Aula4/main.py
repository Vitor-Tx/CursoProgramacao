'''

    --------
    Recursão
    --------

 	- chama uma função dentro dela mesma

  	def funcao(num)
   		if(num > 10):
	 		return num
		return funcao(num + 1)


    ----------
    Exercícios
    ----------

    - fibonacci(recursivo e com laço)
    - inverter uma lista(e string)
    - fatorial
    - 




'''

def funcao(num):
	if(num > 10):
		return num
	return funcao(num + 1)

def fibonacci(num):
	if(num < 2):
		return num
	return fibonacci(num - 1) + fibonacci(num - 2)


def reverse(lista):
	listaRev = ""
	i = len(lista)
	while(i > 0):
		i = i - 1
		listaRev = listaRev + lista[i]
	
	print(listaRev)


reverse("paralelepipedo")