#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char *c = get_string("c: ");
    char *r = malloc(strlen(c) + 1);
    if (r == NULL)
    {
        return 1;
    }
    strcpy(r, c);
    if (strlen(c) > 0)
    {
        *r = toupper(*r);
    }
    printf("%s\n", c);
    printf("%s\n", r);
    
    free(r);
}