
import sys


def es_letra(c: str) -> bool:
    # letra mayus o minus, sin misterio.
    return ("a" <= c <= "z") or ("A" <= c <= "Z")


def es_digito(c: str) -> bool:
    # solo 0-9
    return "0" <= c <= "9"


def afd_identificador(cadena: str) -> bool:
    # AFD para [A-Za-z][A-Za-z0-9]*
    # q0: inicio, tengo que leer una letra pa saber
    # q1: aceptacion, aqui puedo seguir con letra o digito

    # cadena vacia no me sirve pa nada
    if cadena == "":
        return False

    estado = "q0" # inicianding

    for c in cadena:
        if estado == "q0":
            # primera posicion: obligatoriamente letra, o se estalla el mundo
            if es_letra(c):
                estado = "q1"
            else:
                return False
        elif estado == "q1":
            # ya en q1, me quedo en q1 si viene letra o digito, estamos en la segunda parte de la clausula de Kleene, y como es tan sencillo es mejor implementarlo por if
            if es_letra(c) or es_digito(c):
                estado = "q1"
            else:
                # cualquier simbolo raro q no sea de esta familia, de mi linda y pristina expresion regular, pues le rechazamos
                return False

    return estado == "q1"


def AFD(cadena):
    # Lo dejo igual que en punto1: esta funcion devuelve aceptado o No aceptado.
    return "aceptado" if afd_identificador(cadena) else "No aceptado"


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Uso: python3 punto2.py archivo_entrada.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]

    try:
        # Leo linea por linea para que puedas meter muchas pruebas en un txt.
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            for linea in f:
                cadena = linea.strip()
                if cadena:
                    resultado = AFD(cadena)
                    print(f"Cadena '{cadena}': {resultado}")
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
        sys.exit(1)
