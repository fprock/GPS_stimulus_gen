# Generated from /home/chrispy/PycharmProjects/GPS_stimulus_gen/ucbinterm.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\65\n\7")
        buf.write("\r\7\16\7\66\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\n\6\nH\n\n\r\n\16\nI\3\13\6\13M\n\13")
        buf.write("\r\13\16\13N\3\f\5\fR\n\f\3\f\3\f\6\fV\n\f\r\f\16\fW\2")
        buf.write("\2\r\3\3\5\4\7\5\t\2\13\2\r\6\17\7\21\b\23\t\25\n\27\13")
        buf.write("\3\2\5\3\2\62;\4\2\62;CH\5\2\f\f\17\17\"\"\2\\\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3")
        buf.write("\31\3\2\2\2\5(\3\2\2\2\7-\3\2\2\2\t/\3\2\2\2\13\61\3\2")
        buf.write("\2\2\r\64\3\2\2\2\17:\3\2\2\2\21C\3\2\2\2\23G\3\2\2\2")
        buf.write("\25L\3\2\2\2\27U\3\2\2\2\31\32\7>\2\2\32\33\7>\2\2\33")
        buf.write("\34\7>\2\2\34\35\7\"\2\2\35\36\7P\2\2\36\37\7g\2\2\37")
        buf.write(" \7y\2\2 !\7\"\2\2!\"\7G\2\2\"#\7r\2\2#$\7q\2\2$%\7e\2")
        buf.write("\2%&\7j\2\2&\'\7\"\2\2\'\4\3\2\2\2()\7\"\2\2)*\7@\2\2")
        buf.write("*+\7@\2\2+,\7@\2\2,\6\3\2\2\2-.\7\"\2\2.\b\3\2\2\2/\60")
        buf.write("\t\2\2\2\60\n\3\2\2\2\61\62\t\3\2\2\62\f\3\2\2\2\63\65")
        buf.write("\7\"\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66")
        buf.write("\67\3\2\2\2\678\3\2\2\289\b\7\2\29\16\3\2\2\2:;\5\t\5")
        buf.write("\2;<\5\t\5\2<=\7<\2\2=>\5\t\5\2>?\5\t\5\2?@\7<\2\2@A\5")
        buf.write("\t\5\2AB\5\t\5\2B\20\3\2\2\2CD\5\13\6\2DE\5\13\6\2E\22")
        buf.write("\3\2\2\2FH\5\t\5\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2")
        buf.write("\2\2J\24\3\2\2\2KM\n\4\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2")
        buf.write("\2NO\3\2\2\2O\26\3\2\2\2PR\7\17\2\2QP\3\2\2\2QR\3\2\2")
        buf.write("\2RS\3\2\2\2SV\7\f\2\2TV\7\17\2\2UQ\3\2\2\2UT\3\2\2\2")
        buf.write("VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\30\3\2\2\2\t\2\66INQU")
        buf.write("W\3\b\2\2")
        return buf.getvalue()


class ucbintermLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    WHITE = 4
    TIME = 5
    HEX_VAL = 6
    INDEX = 7
    TEXT = 8
    NEWLINE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<<< New Epoch '", "' >>>'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "WHITE", "TIME", "HEX_VAL", "INDEX", "TEXT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "DIGIT", "HEX_DIG", "WHITE", "TIME", 
                  "HEX_VAL", "INDEX", "TEXT", "NEWLINE" ]

    grammarFileName = "ucbinterm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


