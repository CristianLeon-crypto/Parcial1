grammar Fibo;

// Regla inicial
prog:   expr EOF ;

// Regla para reconocer FIBO(n)
expr:   'FIBO' '(' INT ')' ;

// Reglas de léxico
INT :   [0-9]+ ;
WS  :   [ \t\r\n]+ -> skip ; // Ignorar espacios y saltos de línea