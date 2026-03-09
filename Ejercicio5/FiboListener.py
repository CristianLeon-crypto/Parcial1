# Generated from Fibo.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FiboParser import FiboParser
else:
    from FiboParser import FiboParser

# This class defines a complete listener for a parse tree produced by FiboParser.
class FiboListener(ParseTreeListener):

    # Enter a parse tree produced by FiboParser#prog.
    def enterProg(self, ctx:FiboParser.ProgContext):
        pass

    # Exit a parse tree produced by FiboParser#prog.
    def exitProg(self, ctx:FiboParser.ProgContext):
        pass


    # Enter a parse tree produced by FiboParser#expr.
    def enterExpr(self, ctx:FiboParser.ExprContext):
        pass

    # Exit a parse tree produced by FiboParser#expr.
    def exitExpr(self, ctx:FiboParser.ExprContext):
        pass



del FiboParser