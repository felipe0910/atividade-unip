// #include <stdio.h>

// int main()
// {
//     float np1, np2, media;      // Declara 3 variáveis do tipo float.
//                                 // Na Linguagem C sou obrigado a declarar as
//                                 // variáveis. Em Python não sou obrigado.
//     printf( "\n Programa de calculo da media do(a) aluno(a): \n" );
//     printf( " Digite a nota NP1: " );   // Exibe a mensagem pedindo a nota.
//     scanf( "%f", &np1 );        // Obtém a nota digitada no teclado.
//                                 // % na string é o operador de formatação.
//                                 // %f para número real ( float ).
//                                 // %d para número inteiro ( int ).
//     // Exercício: Escreva o código para solicitar a nota NP2:
//     printf( " Digite a nota NP2: " );
//     scanf( "%f", &np2 );        // & é operador de endereço. Passa para
//                                 // scanf() o endereço da variável np2.
//     media= ( np1 + np2 ) / 2;   // Calcula a média e atribui à variável media.
    
//     printf( " Media = %.2f \n", media );  // Exibe média com 2 casas decimais.

//     return 0;
// }

#include <stdio.h>

int main(){

float np1;
float np2;
float pin;


printf("qua nota np1: ");
scanf ("%f", &np1);

printf("qua nota np1: ");
scanf ("%f", &np2);

printf("qual sua nota do pin: ");
scanf ("%f", &pin);

float media= ( 4 * np1 + 4 * np2 + 2 * pin ) / 10;


if (media>=7){
    printf("sua media é : %.2f está APROVADO",media);
}
    
else{
    printf("sua media é : %.2f está REPROVADO",media);

}

return 0;

}