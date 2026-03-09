# Punto 1 - Regex y AFD

## Objetivo
Reconocer movimientos como `p->k4` o `kbp X qn` usando:
- una expresion regular,
- y un AFD implementado en Python.

## Archivo
- `punto1.py`: implementa regex, tokenizacion simple y AFD.
- `punto1.txt`: ejemplos para probar.

## Expresion regular usada

```regex
^\s*(?:p|k|q|r|b|n|kp|qp|krp|qrp|kbp|qbp|knp|qnp)\s*(?:->|[xX])\s*(?:k|q|kr|qr|kb|qb|kn|qn)(?:[1-8])?\s*$
```

Significado:
- origen: pieza en notacion descriptiva (`p`, `kbp`, `qnp`, ...),
- operador: movimiento/captura (`->` o `x`/`X`),
- destino: columna descriptiva (`k`, `qn`, `kb`, ...),
- rango opcional: `1..8`.

## AFD implementado

Definicion formal:
- `Q = {q0, q1, q2, q3, q4}`
- `Sigma = {ORIGEN, OP, DESTINO, RANGO}`
- `q0` estado inicial
- `F = {q3, q4}` estados de aceptacion

Significado de cada estado:
- `q0`: no se ha leido nada valido aun.
- `q1`: ya se leyo un `ORIGEN` valido (por ejemplo `p`, `kbp`, `qnp`).
- `q2`: ya se leyo el operador `OP` (`->` o `x`).
- `q3`: ya se leyo un `DESTINO` valido; aqui la cadena ya puede aceptarse.
- `q4`: se leyo ademas un `RANGO` (`1..8`), tambien es aceptacion.

Funcion de transicion `delta`:
- `delta(q0, ORIGEN) = q1`
- `delta(q1, OP) = q2`
- `delta(q2, DESTINO) = q3`
- `delta(q3, RANGO) = q4`

Las transiciones no definidas van a rechazo (en el codigo se devuelve `No aceptado`).

Ejemplos de recorrido:
- `p->qn` -> tokens `ORIGEN, OP, DESTINO` -> `q0 -> q1 -> q2 -> q3` (aceptado)
- `p->k4` -> tokens `ORIGEN, OP, DESTINO, RANGO` -> `q0 -> q1 -> q2 -> q3 -> q4` (aceptado)
- `p=>k4` -> falla tokenizacion -> rechazo

## Flujo izquierda a derecha (paso a paso)

### Caso valido de ejemplo: `p->k4`
Se lee de izquierda a derecha (duh):
1. `p` -> se reconoce como `ORIGEN` valido -> `q0 -> q1`.
2. `->` -> se reconoce como `OP` valido -> `q1 -> q2`.
3. `k` -> se reconoce como `DESTINO` valido -> `q2 -> q3`.
4. `4` -> se reconoce como `RANGO` valido -> `q3 -> q4`.
5. Fin de cadena en `q4` (estado de aceptacion) -> `aceptado`.

### Caso valido sin rango: `kbp x qn`
1. `kbp` -> `ORIGEN` -> `q0 -> q1`.
2. `x` -> `OP` -> `q1 -> q2`.
3. `qn` -> `DESTINO` -> `q2 -> q3`.
4. Fin de cadena en `q3` (tambien de aceptacion) -> `aceptado`.

### Caso invalido: `p=>k4`
1. `p` -> `ORIGEN` -> `q0 -> q1`.
2. `=>` -> no corresponde a `OP` (`->` o `x`) -> no hay transicion valida.
3. El automata rechaza la cadena -> `No aceptado`.

## Como se procesa una cadena
1. Se eliminan espacios y se pasa a minusculas.
2. Se tokeniza en una secuencia como `['ORIGEN', 'OP', 'DESTINO', 'RANGO']`.
3. El AFD recorre transiciones y reporta `aceptado` o `No aceptado`.
4. Tambien se imprime la secuencia de estados recorrida.

## Como usarlo (comandos)

1. Entrar a la carpeta del punto:

```bash
cd Parciales/Punto_1
```

2. (Opcional) Crear/editar archivo de entrada:

```bash
cat > punto1.txt << 'EOF'
p->k4
kbp X qn
qnp x kb3
p=>k4
EOF
```

3. Ejecutar el programa:

```bash
python3 punto1.py punto1.txt
```

4. Si quieres probar otro archivo:

```bash
python3 punto1.py otro_archivo.txt
```

## Ejecucion

```bash
python3 punto1.py punto1.txt
```

Interpretacion de la salida:
- `Tokens`: simbolos que el AFD procesa (`ORIGEN`, `OP`, `DESTINO`, `RANGO`).
- `Secuencia`: recorrido de estados (`q0 -> ...`).
- `Resultado`: `aceptado` o `No aceptado`.

## Ejemplo de salida real

```txt
Cadena: 'p->k4'
	Tokens: ['ORIGEN', 'OP', 'DESTINO', 'RANGO']
	Secuencia: q0 -> q1 -> q2 -> q3 -> q4
	Resultado: aceptado

Cadena: 'p=>k4'
	Tokens: error de tokenizacion
	Secuencia: q0
	Resultado: No aceptado
```
### Otras cosas
Ahora que lo veo, existen otras maneras de notación
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/40404eb0-c856-4edd-b415-9b1e09cf0340" />

Al finalizar el movimiento si pones en Jaque al rey rival, la notación dice que hay que colocar '+' al final.
