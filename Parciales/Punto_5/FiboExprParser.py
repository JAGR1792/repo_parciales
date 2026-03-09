# Generated from FiboExpr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,13,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,
        2,0,2,0,0,10,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,
        1,0,0,0,7,8,5,1,0,0,8,9,5,2,0,0,9,10,5,4,0,0,10,11,5,3,0,0,11,3,
        1,0,0,0,0
    ]

class FiboExprParser ( Parser ):

    grammarFileName = "FiboExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'FIBO'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "FIBO", "LPAREN", "RPAREN", "INT", "WS" ]

    RULE_input = 0
    RULE_expr = 1

    ruleNames =  [ "input", "expr" ]

    EOF = Token.EOF
    FIBO=1
    LPAREN=2
    RPAREN=3
    INT=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(FiboExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(FiboExprParser.EOF, 0)

        def getRuleIndex(self):
            return FiboExprParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)




    def input_(self):

        localctx = FiboExprParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(FiboExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIBO(self):
            return self.getToken(FiboExprParser.FIBO, 0)

        def LPAREN(self):
            return self.getToken(FiboExprParser.LPAREN, 0)

        def INT(self):
            return self.getToken(FiboExprParser.INT, 0)

        def RPAREN(self):
            return self.getToken(FiboExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return FiboExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = FiboExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(FiboExprParser.FIBO)
            self.state = 8
            self.match(FiboExprParser.LPAREN)
            self.state = 9
            self.match(FiboExprParser.INT)
            self.state = 10
            self.match(FiboExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





