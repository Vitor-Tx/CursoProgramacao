number = 0
number = int(input("Insira um número do sistema decimal: "))
lista = []

while (number != 0):
	lista.append(number % 2)
	print(lista)
	number = int(number / 2)

print("Este é o seu número convertido para o sistema binário:")

for i in lista[::-1]:
	print(i, end="")

