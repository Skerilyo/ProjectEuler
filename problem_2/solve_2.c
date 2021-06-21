#include <stdio.h>

int main() {
    int i = 0;
    int prev = 0;
    int next = 1;
    int tmp = 0;

    while (prev + next < 4000000) {
        tmp = prev + next;
        if (tmp % 2 == 0)
            i += tmp;
        prev = next;
        next = tmp;
    }

    printf("%d", i);
}