#include <stdio.h>
#include <cs50.h>


void print_row(int spaces, int bricks);

int main(void)
{


// get height

    int n;
    do
    {
        n=get_int("Height: ");
    }
    while (n<1);

// print pyramid

    for (int i=0; i<n; i++)
    {
        int spaces=n-i-1;
        int bricks=i+1;
        print_row(spaces, bricks);
    }
}

// print row
void print_row(int spaces, int bricks)
{
    for (int j=0; j<spaces; j++)
    {
        printf(" ");
    }
    for (int k=0; k<bricks; k++)
    {
        printf("#");
    }
    printf("\n");
}
