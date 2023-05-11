#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 9

typedef struct
{
    string name;
    float votes;
}
candidate;
// Array of candidates
candidate candidates[MAX];

// Delimitadores
int candidate_count;
int contador;
int voter_count;
float voter_count2;
int j;
bool verificador_true;
bool verificador_true2;
bool verificador_true3;
bool verificador_true4;
int verificador_winner;

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
            break;
        }
        if ((j == candidate_count - 1) && (verificador_true == false))
        {
            return false;
        }
    }
    candidates[j].votes++;
    return true;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    for (int a = 0; a < candidate_count; a++)
    {
        voter_count2 = voter_count;
        verificador_true3 = candidates[a].votes >= (voter_count2 / 2);
        if (verificador_true3 == true)
        {
            printf("%s\n", candidates[a].name);
        }
        if (voter_count > 4)
        {
            for (int h = 0; h < candidate_count; h++)
            {
                verificador_true4 = strcmp(candidates[a].name, candidates[h].name) == 0;
                if ((candidates[a].votes == candidates[h].votes) && (verificador_true4 == false))
                {
                    printf("%s\n", candidates[a].name);
                }
            }
        }        
    }
    return;
}
add_pairs();
sort_pairs();
lock_pairs();
print_winner();