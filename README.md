# Parciales - Guia General de Ejecucion

Este directorio contiene 5 puntos del parcial.

## Requisitos
- Python 3
- `flex`
- `bison`
- `cc` (o `gcc`)
- `jdk`
- ANTLR4 (comando `antlr4`) para el Punto 5

## Estructura
- `Punto_1`: AFD para movimientos descriptivos de ajedrez
- `Punto_2`: AFD para identificadores
- `Punto_3`: Calculadora en C con Flex/Bison y `sqrt` por Newton-Raphson
- `Punto_4`: Comparacion de rendimiento C vs Python con funcion recursiva
- `Punto_5`: Fibonacci con ANTLR + Python

## Punto 1
```bash
cd Punto_1
python3 punto1.py punto1.txt
```

## Punto 2
```bash
cd Punto_2
python3 punto2.py punto2.txt
```

## Punto 3
Compilar y ejecutar (entrada desde archivo, salida por consola):
```bash
cd Punto_3
bison -d calculadora.y
flex calculadora.l
cc calculadora.tab.c lex.yy.c -lfl -lm
./a.out entrada.txt
```

## Punto 4
Comparacion rapida en un solo comando:
```bash
cd Punto_4
./comparar.sh 35
```

Opcional, manual:
```bash
cc -O2 -o punto4_c punto4.c
./punto4_c 35
python3 punto4.py 35
```

## Punto 5
Si ya generaste ANTLR, ejecuta directamente:
```bash
cd Punto_5
python3 fibo_eval.py
```

Si necesitas regenerar parser/lexer ANTLR:
```bash
cd Punto_5
antlr4 -Dlanguage=Python3 -visitor FiboExpr.g4
python3 fibo_eval.py
```

Ejemplo de entrada por consola:
```txt
FIBO(20)
```
