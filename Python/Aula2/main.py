'''

    --------------
	Vetores/Listas
	--------------

    - Sequências de variáveis do mesmo tipo(vetores) ou de vários tipos(listas).
    - Em python, a implementação mais natural é a de LISTAS.
    - Em C, apenas vetores são usados nativamente. Para usar listas,
      é preciso importar alguma biblioteca ou implementar essa estru
      tura por conta própria. No python, ela já está pronta.
    - As diferenças entre vetores e listas serão estudadas posteriormente.
    - Cada 'casa' do vetor é um índice.
	- O primeiro índice é o índice 0
    - O último índice é o índice n-1(onde n é o tamanho do vetor/lista)
    - É possível criar uma lista de listas(de listas de listas(...))
    - método .append()
    - método .pop()
    - muitos outros métodos:
    https://www.w3schools.com/python/python_ref_list.asp

    Exemplos:

	tupla = (1, 2, 3)
 	00xAB43323415 = endereço de memória
	 v
  	[00xAB43323489][][][][][][][][][][][]
	v
	tupla
 	v
 	[1][2][3]

  
    vet = [1,2,3,4,5,6,7,8,9,10]
    vet2 = [45, -3, -7]
    vet3 = [[1,2,3], ['a', 'b', 'c'], [2.5, 3, -4]]
    vet[0] -> 1 (a primeira casa(ou índice) do vetor é a 0. A última é n-1, 
    onde n é o tamanho do vetor)
    vet[9] -> 10
    vet[-1] -> 10
    vet[-2] -> 9
    len(vet) -> 10
    vet + vet2 = [1,2,3,4,5,6,7,8,9,10, 45, -3, -7]
    vet.pop(2) -> [1,2,4,5,6,7,8,9,10]
    vet.append(-5) -> [1,2,4,5,6,7,8,9,10,-5]

    -------
	Strings
	-------

    - Em python, até mesmo os caracteres são strings. 
    'a', por exemplo, é uma string em python.
    - Também em python, as strings aceitam caracteres
    unicode, ou seja, não se limitam à tabela ASCII.
    - Podemos usar até mesmo emojis nas strings.
    - Dependendo do computador ou do sistema, o padrão
    utilizado é o da tabela ASCII, e é preciso especificar
    o uso do unicode.
    - Os índices podem ser acessados da mesma forma que nos
    vetores/listas.
    - existem vários métodos para manipular strings
    - para adicionar uma string dentro da sua string, basta
    concatená-las utilizando o sinal de +
    - .split()
    - .strip()
    - .replace()
    - muitos outros métodos: 
    https://www.w3schools.com/python/python_ref_string.asp


    Exemplos:

    palavra = 'abc'
    palavra2 = "AaA"
    palavra3 = 'a'
    palavra[0] -> 'a'
    len(palavra) -> 3
    palavra + palavra2 -> 'abcAaA'
    "aaaaa,aaa".split(',') -> ['aaaaa', 'aaa']
    "   aaaaaaaa   ".strip() -> 'aaaaaaaa'
    "   aaaaaaaa   ".replace(' ', '#') -> '###aaaaaaaa###'

    -------
	Tuplas
	-------

    - são IMUTÁVEIS(não podem ser alteradas)
    - Sequências de variáveis de tipos diferentes.
    - Diferentemente de listas e arrays, são representadas
    por parênteses ( ) e não colchetes [ ].
    - Os índices podem ser acessados da mesma forma que nos
    vetores/listas.
    - .count()
    - .index()

    Exemplos: 

    tupla = ('a', 1.5, 3, -47, 'aaaa', [1,2,3,4], ['a', 'b', 'c'], )
    tupla2 = (1, 2, 3) # ninguém disse que tem que ser diferente!
    tupla[5][2] -> 3
    tupla[6][1] -> 'b'
    tupla + tupla2 = ('a', 1.5, 3, -47, 'aaaa', [1,2,3,4], ['a', 'b', 'c'], 1, 2, 3)

    ---------------
	Conjuntos(sets)
	---------------

    - São como tuplas, mas não permitem repetição de elementos, e são mutáveis
    - Podemos converter listas e tuplas para conjuntos usando a
    função set()
    - tem o método .pop()
    - não tem o método .append(), mas tem o .add()
    - métodos relacionados a conjuntos(union, intersection, difference, etc)
    - muitos outros métodos:
    https://www.w3schools.com/python/python_ref_set.asp

    Exemplos:
    - set( (1, 3, -5, 'a', 47, 'b', 3, 'a', -5) ) -> {1, 3, -5, 'a', 47, 'b'}
    - set(1, 2, 4, 4, 92, 6, 92, -5).add(2) -> {1, 2, 4, 92, 6, -5}

    -----------
	Dicionários
	-----------

    - São estruturas de dados bem parecidas com os objetos de
    javaScript.
    - Possuem um padrão de chave:valor
    - Por enquanto, apenas uma introdução.

    Exemplos:

    dic = {'a':'10', 'b':'5', 'c':7, 'd':[1,2,3]}
    dic['a'] -> '10'
    dic['d'] -> [1,2,3]

    -------
	Objetos
	-------

    - Serão melhor compreendidos quando aprendermos 
    Programação Orientada a Objetos.
    - São, em resumo, blocos de informação que armazenam
    dados e ações(métodos).
    - Em python, todas as variáveis são objetos.
    - Não existem objetos em C, pois C não é uma linguagem
    de OO.
    - Todos os tipos de variáveis citados acima são Classes.
    - Cada instância(variável que recebeu um valor) dessas 
    classes é um objeto.
    - Percebam que todos eles possuem métodos(não é um requisito
    para que seja um objeto, mas a maioria deles possui).
    - Os métodos foram definidos nas definições das classes.
    - Objetos em python podem ser mutáveis ou imutáveis
    - Exemplos de objetos mutáveis:
        - Listas
        - Conjuntos
        - Dicionários
        - Classes(podem ser definidas como mutáveis ou imutáveis)
    -  Exemplos de objetos imutáveis:
        - Números (Int, Rational, Float, Decimal, Complex e Booleans)
        - Strings
        - Tuplas
        - Conjuntos congelados
        - Classes(mesma coisa)
    - O que isso significa?
    - Em Python, tudo é um objeto e objetos têm 3 atributos principais:
        - Identidade: É endereço ao qual objeto se refere na memória;
        - Tipo: É o tipo de objeto que foi criado(inteiro, string, lista, etc);
        - Valor: É o valor que o objeto armazena em seu endereço. Por exemplo, 
        uma lista [1,2,3] guarda os números 1, 2 e 3;
        - Enquanto a identidade e o tipo não podem ser alterados, valores podem
        ser alterados para objetos MUTÁVEIS;
        - Alguns objetos armazenam ENDEREÇOS para outros objetos nos seus VALORES,
        como: tuplas, conjuntos e strings;



    Exemplos:


    ------------
	Laços(loops)
	------------

    - while(condição)

    i = 0
    lista = [1,2,3,4,5,6,7,8,9,10]
    while(i < len(lista)):
		print(f"lista = {lista}")
  		print(f"i = {i}")
        lista.pop(0)
        i = i + 1

 	print(f"lista = {lista}")
  	print(f"i = {i}")
    lista -> []

    - for variavel in (objeto iterável)

	tamanho = len(lista)
 	for i in [0,1,2,3,4,5,6,7,8,9]
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

#bin = input("Digite um numero binário: ")
#tamanho = len(bin)
# print(bin[tamanho - 1])
resultado = 0
#for i in range(0, len(bin)):
#	tamanho = tamanho - 1
#	if (bin[tamanho] == '1'):
#		resultado = resultado + 2**i * int(bin[tamanho])
#resultado = resultado + 2**i * int(bin[tamanho])

#print(f"O valor decimal é: {resultado}")


def calculaPotencia(base, expoente):
	resultado = 1
	for i in range(1, expoente + 1):
		resultado = resultado * base
	return resultado


# a = int(input("digite a base: "))
# b = int(input("digite o expoente: "))

# print(f"O resultado da potenciação é: {calculaPotencia(a, b)}")


def imprimePotencias(base, limite):
	for i in range(1, limite + 1):
		print(f'{i}ª potência de {base}: {calculaPotencia(base, i)}')


# codigo principal (vai rodar só o que tá embaixo)
# numero = int(input("Digite um número "))
# expoente = int(input("Digite o expoente "))
# print(f"a variável numero vale {numero}")
'''
	isso é um bloco de comentário.
	nada que está aqui dentro vai 
	ser executado.

 	
'''
# imprimePotencias(numero, expoente)
# print(f"o resultado da potencia é: {calculaPotencia(numero, expoente)}")
''' palavra = "meu pau de oculos"

1ª execução: letra = 'm'
2ª = 'e'
4ª = ' '

concatenação(união de strings)

1ª: "" + 'm'
2ª: "m" + 'e'
3ª: "me" + 'u'
... assim por diante

'''


def minuscula(palavra):
	novaPalavra = ""
	for letra in palavra:
		numero = ord(letra)
		if (numero > 64 and numero < 91):
			letra = chr(ord(letra) + 32)
		novaPalavra = novaPalavra + letra
	print(novaPalavra)


#frase = input("digite uma frase: ")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
tamanho = len(lista)
while (not (lista == [])):
	print(f"lista = {lista}")
	lista.pop(0)

print(lista)