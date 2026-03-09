# Generated from FiboExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FiboExprParser import FiboExprParser
else:
    from FiboExprParser import FiboExprParser

# This class defines a complete listener for a parse tree produced by FiboExprParser.
class FiboExprListener(ParseTreeListener):

    # Enter a parse tree produced by FiboExprParser#input.
    def enterInput(self, ctx:FiboExprParser.InputContext):
        pass

    # Exit a parse tree produced by FiboExprParser#input.
    def exitInput(self, ctx:FiboExprParser.InputContext):
        pass


    # Enter a parse tree produced by FiboExprParser#expr.
    def enterExpr(self, ctx:FiboExprParser.ExprContext):
        pass

    # Exit a parse tree produced by FiboExprParser#expr.
    def exitExpr(self, ctx:FiboExprParser.ExprContext):
        pass



del FiboExprParser