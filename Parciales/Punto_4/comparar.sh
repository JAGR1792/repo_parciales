#!/usr/bin/env bash
set -e

# Uso: ./comparar.sh [n]
# Si no pasas n, usa 35 por defecto.
N=${1:-35}

cc -O2 -o punto4_c punto4.c

c_out=$(./punto4_c "$N")
py_out=$(python3 punto4.py "$N")

echo "=== Resultado C (compilado) ==="
echo "$c_out"
echo
echo "=== Resultado Python (interpretado) ==="
echo "$py_out"
echo

c_ms=$(echo "$c_out" | awk -F': ' '/Tiempo C \(ms\)/ {print $2}')
py_ms=$(echo "$py_out" | awk -F': ' '/Tiempo Python \(ms\)/ {print $2}')

if [[ -n "$c_ms" && -n "$py_ms" ]]; then
  ratio=$(awk -v p="$py_ms" -v c="$c_ms" 'BEGIN { if (c > 0) printf "%.2f", p/c; else print "inf" }')
  echo "Comparacion: Python tarda ~${ratio}x respecto a C (n=$N)"
fi
