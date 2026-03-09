%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Declaración de la función de Newton-Raphson
double newton_sqrt(double a);

// Para errores
void yyerror(const char *s);
int yylex(void);
%}

%union {
    double numero;
}

%token <numero> NUMERO
%token SQRT
%type <numero> expr

%%

inicio:
    expr { printf("Resultado: %.10f\n", $1); }
    ;

expr:
    SQRT '(' NUMERO ')' { $$ = newton_sqrt($3); }
    | NUMERO            { $$ = $1; }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
    yyparse();
    return 0;
}