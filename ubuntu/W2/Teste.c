#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

typedef struct 
{
    string name;
    float NumeroVotos;
}
candidate;

int main (int NC, name[])
{
    candidate person[NC];
    for (int j = 0; j < NC; j++)
    {
        printf("%s\n", person[j].name);
    }
}