#include <stdio.h>
#include <cs50.h>

void meow(int n);


int main(void)
{
    int x = get_int("Quantas vezes você quer que o gato mie? ");
    meow(x);
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Meow\n");
    }
}