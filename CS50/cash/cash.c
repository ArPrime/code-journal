# include <stdio.h>
# include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Exchange= ");
    }
    while (n<0);


    int exchange = n/25;
    int left = n%25;
    exchange = exchange + left/10;
    left = left%10;
    exchange = exchange + left/5;
    left = left%5;
    exchange = exchange + left/1;
    printf("%i\n", exchange);
}
