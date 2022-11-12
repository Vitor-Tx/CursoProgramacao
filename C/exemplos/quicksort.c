#include <stdio.h>

int particiona(int* v, int in, int fim)
{
    int esq, dir, pivo, aux;
    esq = in;
    dir = fim;
    pivo = v[in];

    while(esq < dir)
    {
          while(v[esq] <= pivo) esq++;
          while(v[dir] > pivo) dir--;


          if(esq<dir)
          {
            aux = v[esq];
            v[esq] = v[dir];
            v[dir] = aux;
          }

    }

    v[in] = v[dir];
    v[dir] = pivo;
    return dir;
}

void quickSort(int* v, int in, int fim)
{
    int pivo;
    if(in < fim)
    {
        pivo = particiona(v, in, fim);
        quickSort(v, in, pivo -1);
        quickSort(v, pivo + 1, fim);
    }
}

int main(void) {
  int v[] = {40, -3, 20, 17, 25, 39, 82, 63, -7};
  quickSort(v, 0, 8);
  for(int i = 0; i<9; i++){
	  printf("%d ", v[i]);
  }
  return 0;
}