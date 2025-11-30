#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int calculate_value(string word);

int main(void)
{
    //get input
    string word1 = get_string("Player 1 = ");
    string word2 = get_string("Player 2 = ");

    //calculate value
    int value1 = calculate_value(word1);
    int value2 = calculate_value(word2);
    //compete
    if (value1 > value2)
    {
        printf("Player 1 wins!\n");
    }
    else if (value1 < value2)
    {
        printf("Player 2 wins!\n");
    }
    else if (value1 == value2)
    {
        printf("Tie!\n");
    }
}



// calculate value function

int calculate_value(string word)
{
    int score = 0;
    for (int i=0, n=strlen(word); i<n; i++)
    if (isupper(word[i]))
    {
        score += POINTS[word[i] - 'A'];
    }
    else
    {
        score += POINTS[word[i] - 'a'];
    }
    return score;
}
