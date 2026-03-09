%{
#include <stdio.h>
#include <stdlib.h>

// Declaraciones
double newton_sqrt(double a);
void yyerror(const char *s);
int yylex(void);

// Importante: declarar yyin para que Bison sepa de dónde lee Flex
extern FILE *yyin;
%}

%union {
    double numero;
}

%token <numero> NUMERO
%token SQRT
%type <numero> expr

%%

lista_expr:
    lista_expr expr { printf("Resultado Raiz: %.10f\n", $2); }
    | expr          { printf("Resultado Raiz: %.10f\n", $1); }
    ;

expr:
    SQRT '(' NUMERO ')' { $$ = newton_sqrt($3); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error de sintaxis: %s\n", s);
}

int main(int argc, char **argv) {
    // Abrir el archivo de texto
    FILE *archivo = fopen("entrada.txt", "r");
    if (!archivo) {
        printf("Error: No se pudo abrir el archivo 'entrada.txt'\n");
        return 1;
    }

    // Redirigir la entrada de Flex al archivo
    yyin = archivo;

    // Iniciar el análisis
    yyparse();

    fclose(archivo);
    return 0;
}