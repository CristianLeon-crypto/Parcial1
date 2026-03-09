%{
#include "parser.tab.h"
#include <stdlib.h>

int yywrap(void) {
    return 1;
}
%}

%%
sqrt                { return SQRT; }
[0-9]+(\.[0-9]+)?   { yylval.numero = atof(yytext); return NUMERO; }
\(                  { return '('; }
\)                  { return ')'; }
[ \t\n\r]           ; // Ignorar espacios y saltos de línea
.                   { return yytext[0]; }
%%