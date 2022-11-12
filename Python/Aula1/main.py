'''

	> operadores matemáticos:

	+  -> adição
	-  -> subtração
	*  -> multiplicação
	/  -> divisão
	** -> potenciação


	variavel = alguma coisa -> sinal de atribuição

	> 
	-----------
	Programação
	-----------

	* Preciso ser bom em matemática?
	> Não. Se você sabe somar, subtrair, multiplicar e dividir, já é suficiente.

	* Preciso estudar muito?
	> Depende do que você quer, e depende do seu ritmo de aprendizado. 
	  Eu não estudei muito e aprendi mais com a prática. Mas estudar 
	  te deixa na frente da maioria das pessoas. 30 minutos por dia já 
	  te dá uma vantagem muito grande. Mas não esqueça de praticar também.

	* Os salários são bons?
	> Muito bons. Se você estudar, praticar e sempre tentar se melhorar, 
	  em alguns anos você terá um ótimo emprego, com ótimo salário.

	* Qual linguagem devo estudar?
	> Não faz diferença. Você pode escolher qualquer linguagem que seja usada
	atualmente. Python, C, C++, JavaScript, PHP, C#, etc. Python é mais fácil 
	de aprender quando se está começando, por esconder vários dos conceitos 
	iniciais.

	* É muita coisa pra aprender, como vou decorar tudo isso?
	> Você não precisa decorar nada. Você precisa entender e praticar
	os conceitos fundamentais, e o resto você também aprende e se acostuma.

	> Coisas  específicas de alguma linguagem ou tecnologia, você pode pesquisar
	no google, no stackoverflow, nas documentações, etc. Nem programadores
	profisionais decoram tudo. Eles também usam o google.

	> Muitas das coisas que você estudar e praticar vão simplesmente ficar no
	seu cérebro automaticamente, enquanto você estiver usando elas. Da mesma forma
	que depois que você se acostuma a dirigir, você faz a muitas coisas 
	automaticamente. 

	------------------------------
	Qual a linguagem do computador
	------------------------------

	* O computador entende binário
	* Ele armazena dados na memória em binário

	bit -> 0 ou 1
	byte -> 8 bits

 	ex. de byte: 00101100

	* Convertendo binário pra decimal

 	893(decimal) -> cada casa representa um expoente de 10
	
	1110 -> cada casa representa um expoente de 2, contando a partir de 0:
    


	> A primeira casa(começando da direita) = 2^0 * 1 se for 1, OU 2^0 * 0 se for 0
	> A segunda casa = 2^1 * 1 ou 2^1 * 0
	> Terceira = 2^2 * 1 ou 2^2 * 0
	... assim por diante

	Depois, é só fazer a soma desses valores:

	1110 = (da direita pra esquerda) 2^0 * 0 + 2^1 * 1 + 2^2 * 1 + 2^3 * 1
	0 + 2 + 4 + 8 = 14

	A mesma lógica existe em decimal, só que na base 10:

	881 = 10^0 * 1 + 10^1 * 8 + 10^2 * 8
	881 = 1 + 80 + 800

 	ex. para fixar: 110100110101

  	2^0*1 + 2^1*0 + 2^2*1 + 2^3*0 + 2^4*1 + 2^5*1 + 2^6*0 + 2^7*0 + 2^8*1 + 2^9*0 + 2^10*1 + 2^11*1 
    1 + 0 + 4 + 0 + 16 + 32 + 0 + 0 + 256 + 0 + 1024 + 2048 = 3381

	3381 = 10^0*1 + 10^1*8 + 10^2*3 + 10^3*3   

 	Como converter decimal pra binário 
	vai dividindo por 2 e pegando o resto
    3381/2(resto 1)
	organiza os restos de tras pra frente, e vc terá seu binário

	------------------------------------
	O que é uma linguagem de programação
	------------------------------------

	Resumidamente, linguagens de programação são maneiras de nos comunicarmos com 
	o computador. Mas o computador só entende binário. O que acontece, então?

	* Compilador: Cria um arquivo de código binário a partir do arquivo de código
	da linguagem de programação. Exemplos de linguagens compiladas: Java, C e C++ .

	* Interpretador: Lê o código da linguagem linha a linha e vai traduzindo pro 
	computador, uma linha por vez. Não gera arquivo, então sempre que você rodar
	o programa, o interpretador vai ter que ler tudo denovo. Exemplos de linguagens 
	interpretadas: Python e JavaScript.
	
	---------
	Variáveis
	---------

	* Variável = bloco na memória do computador que armazena um valor
	
	* Tipos de variaveis: 
		> int(inteiro) -> 0, 2, -3, -10, 1000000
		> float(racional) -> 0.2, 0, 1, 2.5, -1000000.53223, 0.345
		> double(racional, com mais espaço) -> mesma coisa do float, com mais espaço 
		> char(caractere) -> 'a', '5', 'r', 'R', ':', '\n'(enter, pula linha)
		> string(sequência de caracteres) ->  "oiiiiiiii"
		> vetores(sequência de dados do mesmo tipo) -> [0, 1, 3, 4, 65, -12]
		> listas(mesma coisa dos vetores, com implementação diferente)
		> tuplas(sequências de dados de tipos diferentes) -> (0, "adas", 'a', 2.3, -10.54)
		> muitos outros tipos

	* Inteiro(int) -> 4 bytes = 32 bits

	2^32 = 4294967296 inteiros possíveis(-2147483648 a 2147483647)
	Nos inteiros, o primeiro bit representa o sinal:
	0 = +
	1 = -
	00000000000000000000000000000000 = 0
	11111111111111111111111111111111 = -2147483648
	01111111111111111111111111111111 = 2147483647
	6								 = 0110 
	18								 = 010010
	42								 = 0101010
	90								 = 01011010
	999								 = 01111100111

	110 = 00000000000000000000000000000110	

	* Nota: A representação dos inteiros com sinal, a depender 
	do tipo de computador, geralmente usa uma notação chamada
	"complemento de dois", que é um pouco mais complexa. Vou 
	te ensinar sobre isso depois, mas não faz diferença agora e 
	não vai mudar em nada que você for usar, é só uma informação 
	que vai te ajudar a entender, no futuro, um pouco mais de 
	como engenheiros do passado descobriram formas mais eficientes 
	de representar números no computador.

	* Exemplos de inteiros:

	2, 3, 4, 10, -57, -32423423

	* Caractere(char) -> 1 byte (8 bits)

	Pode ser considerado um inteiro com menos espaço e representado 
	pela tabela ascii 

	Não tem o bit de sinal

	2 ^ 8 = 256 caracteres possíveis(0 a 255)
	00000000 = 0
	00000001 = 1
	11111111 = 255

	* Tabela ascii = 256 caracteres, do 0 ao 255
	Link: https://3.bp.blogspot.com/-YEtjmpFpUxg/XDSZdbDLEdI/AAAAAAAAAdg/OA5jjcGCYMcUjeV-TOpXej7TqukHZpC8QCLcBGAs/s640/ascii.png

	* Exemplos de caracteres:

	48 = '0'
	65 = 'A'
	97 = 'a'

	* E os outros tipos?

	São mais complexos de explicar as representações, 
	então vou te ensinar no futuro.

	-------
	Funções
	-------

	Função é um bloco de código. São criadas principalmente
	pra não termos que ficar repetindo código várias vezes,
	e isso economiza tempo e deixa o código mais "resumido".

	* Criando a função

	def funcao(parametro):
		codigo da funcao
		return valorQueAFuncaoDevolve	

	a = 10
	b = funcao(a)

	> def: palavra que indica que você está criando uma função

	> Parâmetros: as variáveis que recebem os valores que você 
	  passa pra função. No exemplo acima, só tem um parâmetro,
	  chamado "parametro"

	> Argumentos: os valores que você passa pra função quando 
	  chama ela no código.

	> return: devolve um valor pra variável que estiver recebendo
	  a "saída" da função, se existir.

	Exemplo:

	def multiplica(numero1, numero2):
		resultado = numero1 * numero2
		return resultado

	* Chamando a função 

	a = 10
	b = 15
	c = multiplica(a, b) # chamada da função multiplica, recebendo a e b, com c recebendo o valor de retorno da função
	print(c) # Função que "imprime" o valor da variável c na tela, mas nenhuma variável está recebendo o valor de retorno

	Dica: em python, você pode usar a # ou ''' ''' pra fazer "comentários"
	no seu código. Comentários são textos que o compilador/interpretador vai 
	ignorar, e não fazem nada no seu programa. A # serve pra comentários de 
	uma linha, e as ''' ''' pra comentários de múltiplas linhas. Comentários
	também existem em outras linguagens.

	--------------------
	Desvios Condicionais
	--------------------

	* Desvios condicionais fazem com que seu programa tenha comportamentos
	diferentes, dependendo do que acontecer.

	Imagine que você quer que o programa diga que o usuário digitou um número
	negativo quando ele realmente digitar um número negativo, e dizer que ele
	digitou um número positivo, quando realmente digitar um número positivo:

	> Digito -3
	> O programa diz: "Você digitou um número negativo!"
	> Digito 2
	> O programa diz: "Você digitou um número positivo!"

	Como fazer isso? Utilizando desvios condicionais.

	* if -> tradução para o português: "se"
	* else -> tradução: "se não"
 	* elif -> else if

	* Sintaxe:

	if(numero negativo):
		código
	else:
		outro código

	* Exemplo:

	numero = int(input("Digite um numero "))
	if(numero < 0): #se o número digitado for menor que 0, ou seja, negativo
		print("Você digitou um número negativo")
	else: # se não é menor do que 0, então é positivo com certeza
		print("Você digitou um número positivo!")

	> operadores lógicos

	>  -> maior que
	<  -> menor que
	>= -> maior ou igual a
	<= -> menor ou igual a
	== -> igual a
	&& -> "E" lógico. No python, ele é escrito assim: and
	|| -> "OU" lógico. No python, ele é escrito assim: or
	!  -> "Não" lógico. No python, ele é escrito assim: not

	a = 10
	if(a < 10): # se a for menor do que 10 -> falso

	if(a <= 10): # se a for menor ou igual a 10 -> verdadeiro

	if(a < 10 or a == 10) # se a for menor que 10 ou se a for igual a 10(mesma coisa do de cima) -> verdadeiro

	if(a < 10 and a == 10) # se a for menor que 10 E se a for igual a 10 -> falso

	if(not (a < 10 and a == 10)) # contrário da operação acima -> verdadeiro

	------------------
	Laços de repetição
	------------------

	Laços de repetição servem para executar o mesmo código
	várias vezes seguidas, sem que você precise ficar copiando 
	e colando ele.

	* limite do laço:
	* iterações:

	[0,1,2,3..14]
	for i in range(0, 15):
		if(i < 3):
			print("menor do que 3")
		elif(i < 6):
			print("seila mano")
		else("chegou no 15 ainda nao")

	------------------------
	Entrada e saída de dados
	------------------------

	* input() -> entrada (digitar algo e salvar em uma variavel)
	* print() -> saída   (imprimir algo na tela)


	variavel = 10

	print(variavel)
		resultado = 10
	print("frase")
		resultado = frase
	print(f'frase variavel')
		resultado = frase variavel

	* print(f'frase {variavel}')
		resultado: frase 10

 	a = 120
	print("frase a")
 	 -> frase a
   	print(f"frase {a}")
	 -> frase 120
  	print("frase {a}\nfrase")
   	 -> frase {a}
	    frase
	-------------------
	Exemplo de programa
	-------------------

	* Imprimir as potências de 0 a 10 de um número

	* Calcula potência

	* Transformar todas as letras de uma string em minusculas

	* 

'''

# definição da função


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


#codigo principal (vai rodar só o que tá embaixo)
#numero = int(input("Digite um número "))
#expoente = int(input("Digite o expoente "))
#print(f"a variável numero vale {numero}")
'''
	isso é um bloco de comentário.
	nada que está aqui dentro vai 
	ser executado.

 	
'''
#imprimePotencias(numero, expoente)
#print(f"o resultado da potencia é: {calculaPotencia(numero, expoente)}")
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
''' def minuscula(palavra):
	novaPalavra = ""
	for letra in palavra:
		numero = ord(letra)
		if(numero > 64 and numero < 91):
			letra = chr(ord(letra) + 32)
		novaPalavra = novaPalavra + letra
	print(novaPalavra)
	
frase = input("digite uma frase: ")

minuscula(frase) '''


def multiplica(numero1, numero2):
    resultado = numero1 * numero2
    print(resultado)
    return resultado


#a = int(input("Digite um numero: "))
#numero1 = 56
#b = 15
#c = multiplica(a, b)

i = 0
lista = [1,2,3,4,5,6,7,8,9,10]
tamanho = len(lista)
while(i < tamanho):
	print(f"lista = {lista}")
	print(f"i = {i}")
	lista.pop(0)
	i = i + 1

print(f"lista = {lista}")
print(f"i = {i}")
