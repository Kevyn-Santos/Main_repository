#include <stdio.h>
#include <stdlib.h>

int main(){
    int numeros[5], par[5], impar[5], i;

    for(i=0; i<=4; i++){
        printf("Escreva um numero\n");
        scanf("%i", &numeros[i]);
    }
    printf("os numeros informados foram:\n");
    for(i=0; i<=4; i++){
        printf("%i\n", numeros[i]);
    }
    
}