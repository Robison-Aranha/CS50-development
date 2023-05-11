#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main(void)
{
    char *c = get_string("c: ");
    char *t = get_string("t: ");
    
    if (strcmp(c, t) == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}