#include <stdio.h>

int somar(int b, int a){
	return a + b;
}

struct objeto {
 int a;
 
}

/*
	variavel = bloco na memoria do computador
	bit -> 0 ou 1
	byte -> 8 bits
	inteiro(int) -> 4 bytes = 32 bits
	char(caractere) -> 1 byte (8 bits)

	tabela ascii = 256 caracteres, do 0 ao 256

	
    2 ^ 8 = 256
	00000000 = 0
	00000001 = 1
	11111111 = 255

	tipos de variaveis: 
		int(inteiro) -> 0, 2, -3, -10, 1000000
		float(racional) -> 0.2, 0, 1, 2.5, 1000000.53223, 0.345
		double(racional, com mais espaço) -> mesma coisa do float, com mais espaço 
		char(caractere) = 'a', '5', 'r', 'R', ':', '\n'(enter, pula linha)
		string(varios caracteres): char[20] = "oiiiiiiii\0"(pode ter 19 caracteres + o \0)

	tipodaFunçao nomeDaFuncao(tipoDoArgumento nomeDoArgumento){
		codigo da funçao;
		return valor;
	}
*/


int main(void) {

  int a = 30;
  int b = 15;
  int c = 7;
  int d = 20;
  int e = -15;
  
  a = somar(a,b);

  printf("soma de a \n\ne b vale %d\n", a);

  scanf("%d", &a);
  return 0;
}