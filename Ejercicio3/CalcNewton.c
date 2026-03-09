#include <math.h>

double newton_sqrt(double a) {
    if (a < 0) return 0.0 / 0.0; 
    if (a == 0) return 0;

    double x = a / 2.0; // Estimación inicial como en tu repo
    double tolerancia = 1e-10;
    int max_iter = 1000;
    
    for (int i = 0; i < max_iter; i++) {
        double x_nuevo = 0.5 * (x + a / x);
        if (fabs(x_nuevo - x) < tolerancia) {
            return x_nuevo;
        }
        x = x_nuevo;
    }
    return x;
}