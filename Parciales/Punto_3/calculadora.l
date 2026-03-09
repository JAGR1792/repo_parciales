%{
#include <stdlib.h>
#include "calculadora.tab.h"
%}

%%
[ \t\r]+                    ;
"sqrt"                      { return SQRT; }
[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)? {
                              yylval.num = atof(yytext);
                              return NUMBER;
                            }
"+"                         { return '+'; }
"-"                         { return '-'; }
"*"                         { return '*'; }
"/"                         { return '/'; }
"("                         { return '('; }
")"                         { return ')'; }
\n                          { return EOL; }
.                           { return yytext[0]; }
%%

int yywrap(void) {
    return 1;
}
