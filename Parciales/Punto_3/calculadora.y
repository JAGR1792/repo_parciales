%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int yylex(void);
void yyerror(const char *s);
extern FILE *yyin;

static double newton_sqrt(double x) {
    if (x < 0.0) {
        fprintf(stderr, "Error: sqrt no definida para negativos, y NO QUIERO HACER IMAGINARIOS, GRACIAS        bison -d calculadora.y
        flex calculadora.l
        cc calculadora.tab.c lex.yy.c -lfl -lm
        ./a.out entrada.txt (%.10g)\n", x);
        return NAN;
    }
    if (x == 0.0) {
        return 0.0;
    }

    // la saque de su github profe, traduciendolo obviamente de Python a C.
    double tolerancia = 1e-10;
    int max_iter = 1000;
    double g = x / 2.0;  // estimacion inicial

    for (int i = 0; i < max_iter; i++) {
        if (g == 0.0) {
            g = 1.0;
        }

        double siguiente = 0.5 * (g + x / g);

        if (fabs(siguiente - g) < tolerancia) {
            return siguiente;
        }

        g = siguiente;
    }

    return g;
}
%}

%union {
    double num;
}

%token <num> NUMBER
%token SQRT EOL
%type <num> expr

%left '+' '-'
%left '*' '/'
%right UMINUS

%%
input:
      /* vacio */
    | input line
    ;

line:
      EOL
    | expr EOL { printf("= %.10g\n", $1); }
    ;

expr:
      expr '+' expr      { $$ = $1 + $3; }
    | expr '-' expr      { $$ = $1 - $3; }
    | expr '*' expr      { $$ = $1 * $3; }
    | expr '/' expr      { $$ = $1 / $3; }
    | '-' expr %prec UMINUS { $$ = -$2; }
    | '(' expr ')'       { $$ = $2; }
    | SQRT '(' expr ')'  { $$ = newton_sqrt($3); }
    | NUMBER             { $$ = $1; }
    ;
%%

void yyerror(const char *s) {
    fprintf(stderr, "Error de parseo: %s\n", s);
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s entrada.txt\n", argv[0]);
        return 1;
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
        perror("No se pudo abrir el archivo de entrada");
        return 1;
    }

    yyparse();
    fclose(yyin);
    return 0;
}
