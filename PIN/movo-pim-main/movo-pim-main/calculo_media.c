#include <stdio.h>

int main() {
    float np1, np2, pim, media;

    if (scanf("%f %f %f", &np1, &np2, &pim) != 3) {
        printf("ERRO");
        return 1;
    }

    media = (4 * np1 + 4 * np2 + 2 * pim) / 10.0;

    if (media >= 7.0)
        printf("%.2f\nAprovado", media);
    else if (media >= 5.0)
        printf("%.2f\nRecuperacao", media);
    else
        printf("%.2f\nReprovado", media);

    return 0;
}
