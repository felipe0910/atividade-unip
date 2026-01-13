#include <stdio.h>
#include <math.h>



int main() {
    float a, b, c, delta, x, x1, x2;

    printf("Digite o valor do parametro a: ");
    scanf("%f", &a);

    printf("Digite o valor do parametro b: ");
    scanf("%f", &b);

    printf("Digite o valor do parametro c: ");
    scanf("%f", &c);

    if (a == 0) {
        if (b == 0) {
            printf("\nEquacao impossivel de resolver\n");
        } else {
            x = -c / b;
            printf("\nSolucao unica: x = %.2f\n", x);
        }
    } else {
        delta = b * b - 4 * a * c;

        if (delta < 0) {
            printf("\nNao existe solucao real\n");
        } else {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);
            printf("\nSolucao 1: x1 = %.2f\n", x1);
            printf("Solucao 2: x2 = %.2f\n", x2);
        }
    }

    return 0;
}
