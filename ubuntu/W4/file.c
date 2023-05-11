#include <cs50.h>
#include <string.h>
#include <stdio.h>

int main(void)
{
    FILE *file = fopen("book_name.cvs", "a");
    if (file == NULL)
    {
        return 1;
    }
    
    char *nome = get_string("Nome: ");
    char *idade = get_string("Idade: ");
    
    fprintf(file, "%s, %s\n", nome, idade);
    
    fclose(file);
}