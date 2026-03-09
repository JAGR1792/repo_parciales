import re
import sys

# Regex de apoyo: misma idea del AFD pero en una sola expresion
REGEX_AJEDREZ = re.compile(
    r"^\s*(?:p|k|q|r|b|n|kp|qp|krp|qrp|kbp|qbp|knp|qnp)\s*(?:->|[xX])\s*(?:k|q|kr|qr|kb|qb|kn|qn)(?:[1-8])?\s*$",
    re.IGNORECASE,
)

# Lo que acepto como origen (es quién se mueve)
PIEZAS_ORIGEN = {"p", "k", "q", "r", "b", "n", "kp", "qp", "krp", "qrp", "kbp", "qbp", "knp", "qnp"}
# Lo que acepto como destino descriptivo.
DESTINOS = {"k", "q", "kr", "qr", "kb", "qb", "kn", "qn"}


def a_tokens(cadena):
    # esto es porque no quiero hacer más cosas, mejor tomar solo minusculas como validas incluso si me tiran mayusculas
    texto = "".join(cadena.lower().split())

    # Si hay flecha, a la izquierda del split, estaria todo lo q es el origen el resto, es pues el resto


    if "->" in texto:
        origen, resto = texto.split("->", 1)
    # Si no hay flecha, pruebo split con x, misma logica q arriba
    elif "x" in texto:
        origen, resto = texto.split("x", 1)
    else:
        # Si no hay ni -> ni x, no cumple la forma basica del movimiento y rechazo directo
        return None

    # si el origen no es valido pa q me voy a poner a comprobar el resto, rechazo directo
    if origen not in PIEZAS_ORIGEN:
        return None

    # Si termina en digito, lo tomo como rango (1..8)
    # Ej: resto = "k4" => destino="k", rango="4"
    if len(resto) >= 2 and resto[-1].isdigit():
        destino = resto[:-1]
        rango = resto[-1]
        # si el rango no es valido o el destino no es valido, no me voy a poner a perder el tienpo, rechazo directo
        if rango not in "12345678":
            return None
        if destino not in DESTINOS:
            return None
        # Tokens que leeria el AFD en este caso, donde todo pasa 
        return ["ORIGEN", "OP", "DESTINO", "RANGO"]

    # Caso sin rango, por ejemplo "kbp x qn"
    if resto in DESTINOS:
        return ["ORIGEN", "OP", "DESTINO"]

    return None


def AFD(cadena):
    # Definicion formal del automata
    estados = {"q0", "q1", "q2", "q3", "q4"}
    alfabeto = ("ORIGEN", "OP", "DESTINO", "RANGO")

    # Funcion de transicion.
    # q0 --ORIGEN--> q1 --OP--> q2 --DESTINO--> q3 --RANGO(opcional)--> q4
    F_transiciones = {
        "q0": {"ORIGEN": "q1"},
        "q1": {"OP": "q2"},
        "q2": {"DESTINO": "q3"},
        "q3": {"RANGO": "q4"},
    }

    estado_inicial = "q0"
    estados_finales = {"q3", "q4"}

    # Solo pa dejar explicitos los 5 elementos del AFD en el codigo
    _ = estados, alfabeto

    # Primero convierto la cadena real a simbolos del alfabeto del AFD.
    tokens = a_tokens(cadena)
    if tokens is None:
        return "No aceptado"

    # Recorro transicion por transicion
    estado_actual = estado_inicial
    for simbolo in tokens:
        if simbolo in F_transiciones.get(estado_actual, {}):
            estado_actual = F_transiciones[estado_actual][simbolo]
        else:
            # Si no hay transicion definida, rechazo directo, por eso devolvemos None arriba y ahi se ve como rechazo
            return "No aceptado"

    # Acepto solo si termino en estado final
    return "aceptado" if estado_actual in estados_finales else "No aceptado"


def secuencia_afd(cadena):
    # Esta funcion es para mostrar el flujo: tokens + recorrido de estados
    F_transiciones = {
        "q0": {"ORIGEN": "q1"},
        "q1": {"OP": "q2"},
        "q2": {"DESTINO": "q3"},
        "q3": {"RANGO": "q4"},
    }
    estados_finales = {"q3", "q4"}

    tokens = a_tokens(cadena)
    if tokens is None:
        # Ni siquiera se pudo tokenizar, se ve como rechazo desde q0
        return None, ["q0"], "No aceptado"

    estado_actual = "q0"
    recorrido = [estado_actual]

    for simbolo in tokens:
        if simbolo in F_transiciones.get(estado_actual, {}):
            estado_actual = F_transiciones[estado_actual][simbolo]
            recorrido.append(estado_actual)
        else:
            return tokens, recorrido, "No aceptado"

    resultado = "aceptado" if estado_actual in estados_finales else "No aceptado"
    return tokens, recorrido, resultado


if __name__ == "__main__":
    # Se espera: script + archivo de entrada.
    if len(sys.argv) != 2:
        print("Uso: python3 punto1_ajedrez_afd.py archivo_entrada.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]

    try:
        # Leo cada linea del archivo y pruebo una cadena por vez.
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            for linea in f:
                cadena = linea.strip()
                if cadena:
                    tokens, recorrido, resultado = secuencia_afd(cadena)
                    print(f"Cadena: '{cadena}'")
                    print(f"  Tokens: {tokens if tokens else 'error de tokenizacion'}")
                    print(f"  Secuencia: {' -> '.join(recorrido)}")
                    print(f"  Resultado: {resultado}\n")
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
        sys.exit(1)
