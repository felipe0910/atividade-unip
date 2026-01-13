#include <stdio.h>
#include <math.h>

int main() {
  float numero, raizQuadradada;
  printf(" Digite um numero ");
  scanf( "%f", &numero);
  raizQuadradada = sqrt(numero);
  printf("\n Raiz quadrada de % 2f igual a %.2f\n",numero,raizQuadradada);
   

    return 0;
}
