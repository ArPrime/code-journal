#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool only_digits(string s);
char rotate(char c, int k);

int main(int argc, string argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }


    int key = atoi(argv[1]);


    string plaintext = get_string("plaintext:  ");


    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char ciphertext_char = rotate(plaintext[i], key);
        printf("%c", ciphertext_char);
    }


    printf("\n");
    return 0;
}


bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}


char rotate(char c, int k)
{
    if (isalpha(c))
    {
        char base = isupper(c) ? 'A' : 'a';
        return (char)(((c - base + k) % 26) + base);
    }
    else
    {
        return c;
    }
}
