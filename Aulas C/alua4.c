// #include <stdio.h>

// int main() {
//     int contador = 0;

//     while (contador < 100) {
//         printf("contador = %d\n", contador);
//         contador ++;
//     }
    
//     for(int contador=0; contador<10; contador++)
// {
//     printf("contador = %d\n",contador);
// }
//     return 0;
// }

 #include <stdio.h>
 #include<stdlib.h>

 int main() 
 {
 int contador=10;
 while (contador>=0)
 {
     printf("\n %d",contador);
     contador--;
 }
 printf("contagem decrescentte com for");
 for (int contador =10; contador >=0; contador--)
 {
     printf("\n%d", contador);
 }
 return 0 ; 
 }