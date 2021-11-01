#include <stdio.h>

int main() {
    int a, b, c = 0;
    for (int a = 1; a <= 998; a++) {
        for (int b = a + 1; a + b <= 999; b++) {
            c = 1000 - (a+b);
            if (a * a + b * b == c * c) {
                printf("%d, a:%d, b:%d, c:%d", a * b * c, a, b, c);
                goto end;
            }
        }
    }
    end:
    return 0;
}