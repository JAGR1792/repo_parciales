# Punto 3 - Calculadora con raiz cuadrada en C (Flex y Bison)

Este punto implementa una calculadora que evalua expresiones aritmeticas y `sqrt(expr)`.
La raiz cuadrada se calcula con Newton-Raphson.

Nota: la funcion de Newton-Raphson fue tomada como referencia del GitHub del profesor y traducida de Python a C.

## Archivos
- `calculadora.l`: analizador lexico (Flex).
- `calculadora.y`: parser y evaluacion (Bison), incluye `newton_sqrt`.
- `entrada.txt`: archivo de entrada con expresiones.

## Compilacion

```bash
bison -d calculadora.y
flex calculadora.l
cc calculadora.tab.c lex.yy.c -lfl -lm
```

## Ejecucion

```bash
./a.out entrada.txt
```

## Ejemplo de `entrada.txt`

```txt
sqrt(25)
sqrt(2)
3 + sqrt(9) * 2
(10 - 4) / 3
```

## Salida esperada (aprox.)

```txt
= 5
= 1.414213562
= 9
= 2
```

## Notas
- Si se intenta `sqrt` de un numero negativo, se reporta error y se retorna `nan`.
- Se soportan `+`, `-`, `*`, `/`, parentesis y `sqrt(...)`.
