%{
#include "parser.tab.h"
#include <stdlib.h>

int yywrap(void) {
    return 1;
}
%}
%%
sqrt    { return SQRT; }
[0-9]+(\.[0-9]+)?  { yylval.numero = atof(yytext); return NUMERO; }
\(      { return '('; }
\)      { return ')'; }
[ \t\n] ; // ignorar espacios
.       { return yytext[0]; } // cualquier otro carácter
%%