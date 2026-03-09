# Punto 4 - Comparacion de rendimiento: compilado vs interpretado

Se compara el tiempo de ejecucion de la misma funcion recursiva (`fibonacci`) en:
- C (`punto4.c`) - lenguaje compilado.
- Python (`punto4.py`) - lenguaje interpretado.

Se usa exactamente el mismo algoritmo recursivo en ambos para que la comparacion sea justa.

## Compilacion y ejecucion (comandos basicos)

### C

```bash
cc -O2 -o punto4_c punto4.c
./punto4_c 35
```

### Python

```bash
python3 punto4.py 35
```

## Comparacion rapida en un solo comando

Usa el script `comparar.sh`:

```bash
./comparar.sh 35
```

Si no le pasas parametro, usa `35` por defecto:

```bash
./comparar.sh
```

## Resultados de prueba (ejemplo)

En una prueba tipica con `n=35`, C suele tardar significativamente menos que Python.
Por ejemplo:
- C: decenas de milisegundos.
- Python: cientos o miles de milisegundos.


## Analisis

La diferencia aparece porque:
- C compila a codigo maquina optimizado antes de ejecutarse.
- Python interpreta y administra objetos dinamicos en tiempo de ejecucion.
- La recursion ingenua de Fibonacci amplifica ese costo por la gran cantidad de llamadas.

Para una comparacion justa, se usa exactamente el mismo algoritmo recursivo en ambos lenguajes.
