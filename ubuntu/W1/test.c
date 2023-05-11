#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

int main(void)
{
 long number = get_long("Number: ");
 int a = number / 100000000000000;
 printf("%i\n", a);
}


//4003600000000014