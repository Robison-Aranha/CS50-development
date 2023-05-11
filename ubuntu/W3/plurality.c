#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 9

typedef struct
{
    string name;
    int votes;
}
candidate;
// Array of candidates
candidate candidates[MAX];

// Delimitadores
int candidate_count;
int contador;
int voter_count;
float voter_count2;
int votes2;
int j;
bool verificador_true;
bool verificador_true2;
bool verificador_true3;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (j = 0; j < candidate_count; j++)
    {
        verificador_true = strcmp(name, candidates[j].name) == 0;
        if (verificador_true == true)
        {
            candidates[j].votes++;
            return true;
        }
    }  
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    voter_count2 = voter_count;
    for (int a = 0; a < candidate_count; a++)
    {
        for (int h = 0; h < candidate_count; h++)
        {
            verificador_true3 = candidates[a].votes >= candidates[h].votes;
            if (verificador_true3 == false)
            {
                break;
            }
            if (h == candidate_count - 1)
            {
                for (int r = 0; r < candidate_count; r++)
                {   
                    //verificador_true4 = strcmp(candidates[a].name, candidates[r].name) == 0;
                    if (candidates[a].votes == candidates[r].votes)
                    {
                        printf("%s\n", candidates[r].name);
                    }
                }
                return;
            }
        }
    }
    return;
}