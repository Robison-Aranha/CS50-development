#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
    long number = get_long("Number: ");
    int soma1 = 0;
    int soma2 = 0;
    int counter = 0;
    int num1 = 0;
    long verificação = number;
    long verificação2 = 0;
    long verificação3 = 0;
    int verificação4 = 0;
    while (verificação != 0)
    {
        counter ++;
        verificação = verificação / 10;
    }
    verificação = 1;
    for (int r = 0; r < (counter - 2); r++)
    {
        verificação = verificação * 10;
        num1 = number / verificação; 
    }
    printf("%i\n", num1);
    verificação2 = 100;
    verificação3 = 10;
    soma2 += (number % (verificação2 / 10));
    for (int c = 0; c < (counter / 2); c++)
    {
        verificação4 = ((number % verificação2) / verificação3) * 2;
        soma1 += (verificação4 % 10) + ((verificação4 % 100) / 10);
        soma2 += (number % (verificação2 * 10)) / (verificação3 * 10);
        verificação3 = verificação3 * 100;
        verificação2 = verificação2 * 100;
    }
    soma2 = soma1 + soma2;
    printf("%i", counter / 2);
    if (soma2 % 10 == 0)
    {
        if (counter == 15)
        {
            if (num1 == 34 || num1 == 37)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (counter == 16 || counter == 13)
        {
            if (((num1 % 100) / 10) == 4)
            {
                printf("VISA\n");
            }
            else if (num1 == 51 || num1 == 52 || num1 == 53 || num1 == 54 || num1 == 55)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

