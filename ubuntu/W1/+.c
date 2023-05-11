#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n1 = get_int("Digite um número: ");
    int n2 = get_int("Digite outro número: ");
    printf("A soma entre %i e %i é igual a %i!\n", n1, n2, n1 + n2);
}