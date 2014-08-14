#include <stdio.h>

unsigned long long sumrange(unsigned long long arg)
{
    unsigned long long i, x;
    x = 0;

    for (i = 0; i < arg; i++) {
        x = x + i;
    }
    return x;
}
