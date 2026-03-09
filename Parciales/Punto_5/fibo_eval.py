#!/usr/bin/env python3
"""Punto 5: evaluador de expresiones FIBO(n) con ANTLR4 en Python."""

import sys
from antlr4 import CommonTokenStream, InputStream

from FiboExprLexer import FiboExprLexer
from FiboExprParser import FiboExprParser
from FiboExprVisitor import FiboExprVisitor


class EvalFiboVisitor(FiboExprVisitor):
    def visitInput(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        n = int(ctx.INT().getText())
        if n < 0:
            raise ValueError("n debe ser >= 0")
        return self._fibo_hasta(n)

    @staticmethod
    def _fibo_hasta(limite):
        secuencia = [0]
        a, b = 0, 1
        while b <= limite:
            secuencia.append(b)
            a, b = b, a + b
        return secuencia


def main():
    texto = input("Ingresa expresion (ej. FIBO(20)): ").strip()
    if not texto:
        print("Entrada vacia")
        sys.exit(1)

    lexer = FiboExprLexer(InputStream(texto))
    tokens = CommonTokenStream(lexer)
    parser = FiboExprParser(tokens)
    tree = parser.input_()

    visitor = EvalFiboVisitor()
    resultado = visitor.visit(tree)

    print("Secuencia:", ", ".join(str(x) for x in resultado))


if __name__ == "__main__":
    main()
