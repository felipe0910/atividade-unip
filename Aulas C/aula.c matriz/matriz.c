// Online C compiler to run C program online
#include <stdio.h>

int main() {
  
  char mensagem [] ="aula de linguagem";
  printf ("exibindo em ordem \n");
  
  int pos =0; //posição do caractere 
  
  while (mensagem[ pos ]!='\0')
  {
      ++pos;
  }
  
  printf("\n a string possui %d caracteres. \n ", pos);
  --pos;
  printf("\n ultimo caractere =%c \n", mensagem[pos]);
  
  printf("exibindo em ordem inversa:\n");
  while (pos >=0)
  {
      printf("%c",mensagem[pos]); //posicao exibe caractere decrementa a posicao
      --pos;
  }
    return 0;
}