#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main(int argc, char **argv) {
    int n = 35;
    if (argc > 1) {
        n = atoi(argv[1]);
    }

    struct timespec t1, t2;
    clock_gettime(CLOCK_MONOTONIC, &t1);
    long long resultado = fibonacci(n);
    clock_gettime(CLOCK_MONOTONIC, &t2);

    double ms = (t2.tv_sec - t1.tv_sec) * 1000.0 +
                (t2.tv_nsec - t1.tv_nsec) / 1000000.0;

    printf("Fibonacci(%d) = %lld\n", n, resultado);
    printf("Tiempo C (ms): %.3f\n", ms);

    return 0;
}
