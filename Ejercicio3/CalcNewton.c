#include <math.h>

// Implementación del método de Newton-Raphson para raíz cuadrada
double newton_sqrt(double a) {
    if (a < 0) return 0.0 / 0.0; // NaN
    if (a == 0) return 0;

    double x = a / 2; // estimación inicial
    double tolerancia = 1e-10;
    int max_iter = 1000;
    int i;

    for (i = 0; i < max_iter; i++) {
        double x_nuevo = 0.5 * (x + a / x);
        if (fabs(x_nuevo - x) < tolerancia) {
            return x_nuevo;
        }
        x = x_nuevo;
    }

    return x;
}