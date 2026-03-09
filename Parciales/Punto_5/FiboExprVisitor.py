# Generated from FiboExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FiboExprParser import FiboExprParser
else:
    from FiboExprParser import FiboExprParser

# This class defines a complete generic visitor for a parse tree produced by FiboExprParser.

class FiboExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FiboExprParser#input.
    def visitInput(self, ctx:FiboExprParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FiboExprParser#expr.
    def visitExpr(self, ctx:FiboExprParser.ExprContext):
        return self.visitChildren(ctx)



del FiboExprParser