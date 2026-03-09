grammar FiboExpr;

input: expr EOF;

expr: FIBO LPAREN INT RPAREN;

FIBO: 'FIBO';
LPAREN: '(';
RPAREN: ')';
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
