'''
Converta um número binário pra decimal

dicas:

> coloque pra ler o número binário(não converta pra inteiro)
> pra acessar valores de um vetor/objeto: objeto[valor]
> string é um objeto
> len(objeto) = quantidade de variaveis no objeto/vetor
> começar da direita pra esquerda
> j = j + 1
> y = y - 1

'''

bin = input("Digite um numero binário: ")
tamanho = len(bin)
# print(bin[tamanho - 1])
resultado = 0
for i in range(0, len(bin)):
	tamanho = tamanho - 1
	if (bin[tamanho] == '1'):
		resultado = resultado + 2**i * int(bin[tamanho])
	#resultado = resultado + 2**i * int(bin[tamanho])

print(f"O valor decimal é: {resultado}")
'''

runescape tem gp = moedas

2.147b = max cash stack

spirit shard = 25gp
2.147b de spirit shards

'''
