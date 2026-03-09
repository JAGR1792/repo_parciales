# Punto 5 - Calculadora de Fibonacci con ANTLR (Python)

Se define una gramatica ANTLR para expresiones de la forma `FIBO(n)` y un programa Python que evalua la entrada y devuelve la secuencia Fibonacci hasta ese limite.

## Archivos
- `FiboExpr.g4`: gramatica ANTLR.
- `fibo_eval.py`: evaluador en Python usando visitor.

## Generacion del parser/lexer en Python

Requisito: `antlr-4.x-complete.jar` y `antlr4-python3-runtime`.

```bash
antlr4 -Dlanguage=Python3 -visitor FiboExpr.g4
```

Esto genera archivos como:
- `FiboExprLexer.py`
- `FiboExprParser.py`
- `FiboExprVisitor.py`

## Ejecucion por consola

```bash
python3 fibo_eval.py
```

Entrada de ejemplo:

```txt
FIBO(20)
```

Salida esperada:

```txt
Secuencia: 0, 1, 1, 2, 3, 5, 8, 13
```

## Comandos rapidos (todo junto)

Desde la carpeta `Parciales/Punto_5`:

```bash
antlr4 -Dlanguage=Python3 -visitor FiboExpr.g4
python3 fibo_eval.py
```

Prueba directa en terminal sin escribir manualmente:

```bash
printf 'FIBO(20)\n' | python3 fibo_eval.py
```

## Notas
- La salida incluye todos los Fibonacci `<= n`.
- Si la expresion no cumple la gramatica, ANTLR reporta error de parseo.
