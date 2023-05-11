#include <stdio.h>
#include <cs50.h>

void piramides(int j);

int main(void)
{
    int n;
    do
    {
        n = get_int("Hight: ");
    }
    while (n < 1 || n > 8);
    piramides(n);
}
// Watch anime! they are wonderfull!!!

void piramides(int j)
{
    int verificação = 0;
    for (int i = 0; i < j; i++)
    {
        verificação ++;
        int t = 0;
        for (t = j; t > verificação; t--)
        {
            printf(" ");
        }
        for (int r = 0; r < (verificação * 2); r++)
        {
            printf("#");
            if (r == verificação - 1)
            {
                printf("  ");
            }
        }
        printf("\n");
    }
}