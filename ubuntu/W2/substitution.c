#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void cripto(int cont, string j, string r);

int main(int arg, string arg2[])
{
    if (arg == 2)
    {
        string text = "";
        string crtx = arg2[1];
        int contador = strlen(crtx);
        int verificador2 = 0;
        int verificador3 = 0;
        int verificador4 = 0;
        if (contador == 26)
        {
            bool verificador;
            for (int i = 0; i < contador; i++)
            {
                verificador = isalpha(crtx[i]);
                if (verificador == false)
                {
                    printf("Key only must contain alphabetic characters.\n");
                    return 1;
                }
            }
            for (int y = 0; y < contador; y++)
            {
                if (toupper(crtx[y]) == 65 + verificador4)
                {
                    verificador3++;
                }
                else if (verificador3 >= 2)
                {
                    printf("Key must not contain repeated characters\n");
                    return 1;
                }
                else if (verificador4 == contador)
                {
                    break;
                }
                else if (y == 25)
                {
                    y = 0;
                    verificador4++;
                    verificador3 = 0;
                }
            }
        }
        else
        {
            printf("Key must contain 26 characteres.\n");
            return 1;
        }
        text = get_string("plaintext: ");
        for (int g = 0; g < contador; g++)
        {
            crtx[g] = toupper(crtx[g]);
        }
        contador = strlen(text);
        cripto(contador, crtx, text);
    }
    else
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }
}

void cripto(int cont, string j, string r)
{
    int verificação;
    for (int c = 0; c < cont; c++)
    {
        verificação = j[toupper(r[c]) - 65];
        if (r[c] >= 'A' && r[c] <= 'Z')
        {
            r[c] = toupper(verificação);
        }
        else if (r[c] >= 'a' && r[c] <= 'z')
        {
            r[c] = tolower(verificação);
        }
        else
        {
            r[c] = r[c];
        }
    }
    printf("ciphertext: %s\n", r);
}
