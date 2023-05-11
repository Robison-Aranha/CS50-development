#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int start = 0;
    int end = 0;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);
    do
    {
        end = get_int("End size: ");
    }
    while (end < 9 || end < start);
    int years = 0;
    while (end > start)
    { 
        start += ((start / 3) - (start / 4));
        years ++;
    }
    printf("Years: %i\n", years);
}

