#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    string Text[0];
    float letters = 0;
    float words = 0;
    float sentences = 0;
    float index;
    float L;
    float S;
    Text[0] = get_string("Text: ");
    for (int i = 0; i < strlen(Text[0]); i++)
    {
        if (isalpha(Text[0][i]))
        {
            letters++;
        }
        if (ispunct(Text[0][i]))
        {
            sentences++;
        }
        if (isspace(Text[0][i]))
        {
            words++;
        }
        if ((Text[0][i] == '"') || (Text[0][i] == ',') || (Text[0][i] == '-') || (Text[0][i] == ':'))
        {
            sentences--;
        }
        if (ispunct(Text[0][i]) && (isalpha(Text[0][i + 1])) && (isalpha(Text[0][i - 1])))
        {
            sentences--;
        }
        
    }
    words = words + 1;
    L = (letters /  words) * 100;
    S = (sentences / words) * 100;
    index = (0.0588 * L) - (0.296 * S) - 15.8;
    printf("%f, %f, %f\n", letters, words, sentences);
    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    if ((index > 0) && (index <= 16))
    {
        printf("Grade %.0f\n", round(index));
    }
    if (index < 0)
    {
        printf("Before Grade 1\n");
    }

}