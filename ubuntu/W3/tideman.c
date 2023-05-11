#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }


        record_preferences(ranks);

        printf("\n");
    }
    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    int verificador = 0;
    for (int c = 0; c < candidate_count; c++)
    {
        if (verificador != c)
        {
            if (verificador < c)
            {
                preferences[ranks[verificador]][ranks[c]] += 1;
            }
        }
        if (c == candidate_count - 1)
        {
            verificador++;
            c = -1;
        }
        if (verificador == candidate_count)
        {
            break;
        }
    }
    return;
}



// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    int verificador = 0;
    for (int c = 0; c < candidate_count; c++)
    {
        if (preferences[verificador][c] > preferences[c][verificador])
        {
            pairs[pair_count].winner = verificador;
            pairs[pair_count].loser = c;
            pair_count++;
        }
        if (c == candidate_count - 1)
        {
            verificador++;
            c = -1;
        }
        if (verificador == candidate_count)
        {
            break;
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int verificador = 0;
    int diferença[pair_count];
    int colocação[pair_count];
    int pair2[pair_count];
    int pair3[pair_count];
    int maior = 0;
    for (int c = 0; c < pair_count; c++)
    {
        diferença[c] = preferences[pairs[c].winner][pairs[c].loser] - preferences[pairs[c].loser][pairs[c].winner];
        pair2[c] = pairs[c].winner;
        pair3[c] = pairs[c].loser;
    }
    for (int c = 0; c < pair_count; c++)
    {
        for (int i = 0; i < pair_count; i++)
        {
            if (diferença[i] > maior)
            {
                maior = diferença[i];
                verificador = i;
            }
        }
        colocação[c] = maior;
        diferença[verificador] = 0;
        maior = 0;
    }
    for (int c = 0; c < pair_count; c++)
    {
        for (int i = 0; i < pair_count; i++)
        {
            if (colocação[i] == preferences[pair2[c]][pair3[c]] - preferences[pair3[c]][pair2[c]])
            {
                pairs[i].winner = pair2[c];
                pairs[i].loser = pair3[c];
                colocação[i] = 0;
                break;
            }
        }
    }
    for (int i = 0; i < pair_count; i++)
    {
        printf("%i %i\n", pairs[i].winner, pairs[i].loser);
    }
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    int ciclo = 0;
    for (int c = 0; c < pair_count; c++)
    {
        locked[pairs[c].winner][pairs[c].loser] = true;
        ciclo = pairs[c].loser;
        for (int i = 0; i < pair_count; i++)
        {
            if (locked[ciclo][pairs[i].loser] == true)
            {
                if (ciclo == pairs[c].winner)
                {
                    locked[pairs[c].winner][pairs[c].loser] = false;
                    break;
                }
                ciclo = pairs[i].loser;
                i = -1;
            }
            if (i == pair_count - 1)
            {
                for (int r = 0; r < pair_count; r++)
                {
                    if (ciclo == pairs[r].loser)
                    {
                        for (int j = 1; j <= pair_count; j++)
                        {
                            if (pairs[r + j].winner == pairs[r].winner && locked[pairs[r + j].winner][pairs[r + j].loser] == true)
                            {
                                ciclo = pairs[r + j].loser;
                                i = -1;
                                break;
                            }
                        }
                    }
                }
            }
        }
    }
}

// Print the winner of the election
void print_winner(void)
{
    int win = 0;
    bool verificador = true;
    for (int c = 0; c < candidate_count; c++)
    {
        for (int i = 0; i < candidate_count; i++)
        {
            if (locked[i][c] == false)
            {
                verificador = true;
            }
            else
            {
                verificador = false;
                break;
            }
        }
        if (verificador == true)
        {
            printf("%s\n", candidates[c]);
            break;
        }
    }
}

