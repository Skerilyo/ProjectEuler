#include <stdio.h>

int main() {
    int i = 0;

    for (int j = 0; j < 1000; j++)
        if (!(j%3) || !(j%5))
            i += j;

    printf("%d", i);
}