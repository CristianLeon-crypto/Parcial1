#include <stdio.h>

long long fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 40;
    printf("Calculando Fibonacci de %d en C...\n", n);
    long long resultado = fibonacci(n);
    printf("Resultado: %lld\n", resultado);
    return 0;
}