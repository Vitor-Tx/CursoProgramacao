import math
'''

    REVISÃO AULA2

    ------------
	Laços(loops)
	------------

    - while(condição)

    i = 0
    lista = [1,2,3,4,5,6,7,8,9,10]
	tamanho = len(lista)
    while(i < tamanho):
        lista.pop(0)
        i = i + 1
    lista -> []

    - for variavel in (objeto iterável)

	tamanho = len(lista)
    for i in range(0, tamanho):
        lista.pop(0)
    lista -> []

    - o i começa em 0 e termina em len(lista) - 1, assim como no while
    - range(inicio, fim) é uma função que gera uma sequência de objetos em
    ordem crescente(por padrão), começando de inicio e indo até fim - 1.
    - podemos substituir o range por uma lista, por exemplo:
        for i in [1,2,3,4,5,6,7,8,9,10]:
            print(i) # vai printar um número por linha(incluindo o 10)
    - ou por uma string:
        for i in "aaaaaaaaab342342342342":
            print(i) # vai printar um caractere por linha(incluindo o último)
    - ou por outras funções, objetos e etc. que podem ser iteráveis.
    - break
    - continue
    - break e continue também servem para while

    -------------------------------
	Compreensão de listas em python
	-------------------------------

    - Modo de criar novas listas a partir de sequências e regras
    - Sequências incluem listas, tuplas, strings, conjuntos, etc
    - Independente da entrada, o resultado sempre será uma lista
    - Utiliza laços e desvios condicionais
    - Exemplos:

    [x**2 - 1 for x in range(0, 10)] -> [-1, 0, 3, 8, 15, 24, 35, 48, 63, 80]
    [x.replace(x, '25') for x in "abc"] -> ['25', '25', '25']
    [x**2 -1 for x in range(0, 10) if x%2 == 0] -> [-1, 3, 15, 35, 63]

    - Dica: o operador % retorna o resto da divisão de 2 números inteiros.


    --------------------
	Orientação a objetos
	--------------------

    - De onde vêm os objetos? Das classes

    - O que os objetos têm? Propriedades e métodos.

    > Ex.: de propriedades: Nome, idade, altura, peso e etc.
      -> são dados que os objetos guardam.
    > Ex.: de métodos: imc(), idade(), .append() para listas e etc.
      -> são ações que os objetos podem executar.

    - As classes são como "formas" que definem o que seus objetos podem
      guardar e fazer.

    - Comparação com a vida real: existem espécies de seres vivos e cada
    espécie tem suas características. Essas características são definidas
    no código genético(DNA).

    - Algumas classes podem herdar características de outras classes
    assim como funciona na taxonomia, ou mesmo herança genética de
    grupos familiares.

    - Como criar uma classe?

    class Cachorro:
        # Atributo de classe
        especie = "Canis familiaris"
        pass

    - A palavra pass só é usada para quando você ainda não sabe o que colocar
      na classe. Assim, ao rodar o programa, não ocorrerá erro. Ela também
      pode ser usada em funções.
    
    - Nomes de classes, por consenso, são escritos em CamelCase.

    - Construtores

        def __init__(self, nome, idade, cor, raca):
            self.nome = nome
            self.idade = idade
            self.cor = cor
            self.raca = raca

    - Métodos

        def info(self):
            print(f"Esse cachorro se chama {self.nome}, tem {self.idade} anos de idade é um {self.raca} {self.cor}")

        # def __str__(self):
        def latir():
            print("auau!")

        def rosnar():
            print("grrrr!")
        
    - O que é self?
      Aponta para o próprio objeto(o endereço de memória dele).

    - Atributos de instância vs Atributos de classe


    - Instanciando um objeto da classe Cachorro

      cachorro = Cachorro("Rex", 2, "caramelo", "vira-lata")
	  cachorro2 = Cachorro("Totó", 1, "preto", "vira-lata")

    - Herança de classes
        class PastorAlemao(Cachorro):
            pass

    - Classe pai: Cachorro e Classe filho: PastorAlemao

    - PastorAlemao herda todos os métodos e atributos de Cachorro

    - Método super()

    - Utilizando o super()
'''
'''

    Exemplos de programas
	---------------------

	* Imprimir as potências de 0 a 10 de um número

	* Calcular potência

	* Transformar todas as letras de uma string em minusculas

    * Converter um número binário para decimal

    * Converter um número decimal para binário(desafio)

    * Mais...

dicas(binário pra decimal):

> coloque pra ler o número binário(não converta pra inteiro)
> pra acessar valores de um vetor/objeto: objeto[valor]
> string é um objeto
> len(objeto) = quantidade de variaveis no objeto/vetor
> começar da direita pra esquerda
> j = j + 1
> y = y - 1

'''
'''
decimal pra binário



import math
number = 0
number = int(input("Insira um número do sistema decimal: "))
lista = []

while (number != 0):
	lista.append(number % 2)
	print(lista)
	number = int(math.floor(number / 2))

print("Este é o seu número convertido para o sistema binário:")

for i in lista[::-1]:
	print(i, end="")

'''

#for i in range(0, 100):
#	if((i % 25) == 0):
#		break
#	if(i > 50):
#		break
#	if(i % 2 == 0):
#		continue
#	print(i)

#lista = [x**2 - 1 for x in range(0, 20)]

#lista2 = [(x - 2)**3 for x in lista if x < 15]

#print(lista2)

#print(lista) # -> [-1, 0, 3, 8, 15, 24, 35, 48, 63, 80]
# print([x.replace(x, '25') for x in "abc"])  # -> ['25', '25', '25']
#print([x**2 -1 for x in range(0, 10) if x%2 == 0]) # -> [-1, 3, 15, 35, 63]


def calculaPotencia(base, expoente):
	return base**expoente


def potencia0a10(base):
	for i in range(0, 11):
		print(calculaPotencia(base, i))


def minuscula(palavra):
	novaPalavra = ""
	for letra in palavra:
		numero = ord(letra)
		if (numero > 64 and numero < 91):
			letra = chr(ord(letra) + 32)
		novaPalavra = novaPalavra + letra
	print(novaPalavra)


#minuscula("AAAAABBBASDAD345435sadasdasd546RTDsasws8")


def binToDec(number):
	expoente = 0
	binReverse = number[::-1]
	soma = 0
	for i in binReverse:
		if (i == '0'):
			expoente = expoente + 1
			continue
		soma = soma + 2**expoente
		expoente = expoente + 1

	return soma


def decToBin(number):
	decimal = []
	while (number > 0):
		decimal.append(number % 2)
		number = int(math.floor(number / 2))

	for i in decimal[::-1]:
		print(i, end="")

	print('\n')


class Cachorro:
	# Atributo de classe
	especie = "Canis familiaris"

	def __init__(self, nome, idade, cor, raca):
		self.nome = nome
		self.idade = idade
		self.cor = cor
		self.raca = raca

	def latir(self):
		print("auau!")

	def rosnar(self):
		print("grrrr!")

	def descricao(self):
		print(
		 f'Esse é o {self.nome}, ele tem {self.idade} anos de idade e é um {self.raca} {self.cor}.'
		)




class PastorAlemao(Cachorro):
	def __init__(self, nome, idade, cor):
		super().__init__(nome, idade, cor, "Pastor Alemão")

	def latir(self):
		super().latir()
		print("Woof woof")


cachorro = Cachorro("Rex", 2, "caramelo", "vira-lata")
cachorro2 = PastorAlemao("Marmita", 4, "branco")
cachorro.latir()
cachorro.rosnar()
cachorro2.descricao()
cachorro2.latir()
cachorro2.rosnar()