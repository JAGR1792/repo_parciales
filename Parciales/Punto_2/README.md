# Punto 2 - AFD para identificadores

## Objetivo
Validar identificadores con la forma:

```regex
[A-Za-z][A-Za-z0-9]*
```

Es decir:
- primer caracter: letra,
- siguientes: letras o digitos.

## Archivos
- `punto2.py`: implementacion del AFD y lectura desde archivo.
- `punto2.txt`: archivo de ejemplo con cadenas de prueba.

## Como usarlo (comandos)

1. Entrar a la carpeta:

```bash
cd arciales/Punto_2
```

2. (Opcional) Crear/editar archivo de entrada:

```bash
cat > punto2.txt << 'EOF'
variable
A1
miID2026
9inicio
nombre-apellido
EOF
```

3. Ejecutar:

```bash
python3 punto2.py punto2.txt
```

## Que imprime
Por cada linea del archivo:
- `aceptado` si cumple el AFD.
- `No aceptado` si no cumple.

Ejemplo:

```txt
Cadena 'variable': aceptado
Cadena '9inicio': No aceptado
```
