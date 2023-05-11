// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <ctype.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int number = 0;
// Number of buckets in hash table
const unsigned int N = 676;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int num = hash(word);
    int count = 0;
    if (table[num] != NULL)
    {
        for (node *tmp = table[num]; tmp != NULL; tmp = tmp-> next)
        {
            if (count > 0 && strcasecmp(word, tmp-> word) == 0)
            {
                return true;
            }
            count++;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{   
    int count = ((int) toupper(word[0]) - 65) * 25;
    int num = (int) toupper(word[0]) + (int) toupper(word[1]);
    if (num < 130)
    {
        num = num - 65;
    }
    else
    {
        num = (num - 130) + count;
    }
    return num;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    char palavra[LENGTH + 1];
    FILE *arq = fopen(dictionary, "r");
    if (arq == NULL)
    {
        return false;
    }
    while (fscanf(arq, "%s", palavra) != EOF)
    {
        node *word = malloc(sizeof(node));
        int num = hash(palavra);
        if (table[num] == NULL)
        {
            table[num] = malloc(sizeof(node));
            table[num]-> next = NULL;
        }
        if (table[num]-> next != NULL)
        {
            strcpy(word-> word, palavra);
            word-> next = table[num]-> next;
            table[num]-> next = word;
            number++;
        }
        else
        {
            strcpy(word-> word, palavra);
            table[num]-> next = word;
            word-> next = NULL;
            number++;
        }
    }
    fclose(arq);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return number;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]-> next;
            free(table[i]);
            table[i] = tmp;
        }
    }
    return true;
}
