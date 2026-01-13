#include <stdio.h>

int main() {
    int n;
    printf("Digite um número: ");
    scanf("%d", &n);

    switch (n) {
        case 0:
            printf("ZERO");
            break;
        case 1:
            printf("UM");
            break;
        case 2:
            printf("DOIS");
            break;
        case 3:
        case 4:
            printf("TRES ou QUATRO");
            break;
        case 5:
            printf("CINCO");
            break;
        default:
            printf("SO SEI CONTAR ATE 5");
            break;
    }

    return 0;
}


