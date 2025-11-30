#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int quant_l(string user_input, int length_input);
int quant_w(string user_input, int length_input);
int quant_s(string user_input, int length_input);

int main(void)
{
    // Prompt the user for some text
    string user_input = get_string("Input your text: ");
    int length_input = strlen(user_input);

    // Count the number of letters, words, and sentences in the text
    int num_l = quant_l(user_input, length_input);
    int num_s = quant_s(user_input, length_input);
    int num_w = quant_w(user_input, length_input);


    // Compute the Coleman-Liau index
    float percent_l = (float)num_l / num_w * 100;
    float percent_s = (float)num_s / num_w *100;
    float CL_index = 0.0588 * percent_l - 0.296 * percent_s - 15.8;

    // Print the grade level
    if (CL_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (CL_index < 16)
    {
        printf("Grade %i\n", (int)round(CL_index));
    }
    else
    {
        printf("Grade 16+\n");
    }
}


int quant_s(string user_input, int length_input)
{
    int num_s = 0;
    for (int i=0; i<length_input; i++)
    {
        if (user_input[i] == '.' || user_input[i] == '!' || user_input[i] == '?')
        {
            num_s++;
        }

    }
    return num_s;
}

int quant_l(string user_input, int length_input)
{
    int num_l = 0;
    for (int i=0; i<length_input; i++)
    {
        if (isalpha(user_input[i]))
        {
            num_l++;
        }
    }
    return num_l;
}

int quant_w(string user_input, int length_input)
{
    int num_space = 0;
    for (int i=0; i<length_input; i++)
    if (isspace(user_input[i]))
    {
        num_space++;
    }
    return num_space+1;
}


