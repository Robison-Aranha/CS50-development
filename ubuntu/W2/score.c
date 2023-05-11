#include <stdio.h>
#include <cs50.h>

int  main(void)
{
    int n = get_int("Number os scorres: ");
    int scores[n];
    float r;
    int R;
    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1);
        
    }
    for (int j = 0; j < n ; j++)
    {
            r = r + scores[j];
    }

    printf("media artmetica: %.2f\n", (r / n));
}