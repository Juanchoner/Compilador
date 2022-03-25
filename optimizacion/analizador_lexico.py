'''
Script en python en el cual, se crea la clase de CalculadoraParser para relizar
el analisis sintactico de la mini-calculadora
'''

from sly import Lexer

class CalculadoraLexer(Lexer):
    tokens = {
        ID,
        SUM,
        RES,
        DIV,
        MUT,
        MOD,
        POT,
        ASG,
        COM,
        DIF,
        MRQ,
        MYQ,
        MRI,
        MYI,
        PQA,
        PQC,
        LQA,
        LQC,
        CDT,
        NUM,
        DCI
    }
    ignore = ' \t'


    #Tokens
    ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
    CDT = r"'.*'"
    DCI = r'\d*\.\d+'
    NUM = r'\d+'

    #Simbolos especiales
    SUM = r'\+'
    RES = r'\-'
    POT = r'\*\*'
    MUT = r'\*'
    DIV = r'/'
    MOD = r'%'
    MRI = r'<='
    MYI = r'>='
    COM = r'=='
    ASG = r'='
    DIF = r'!='
    MRQ = r'<'
    MYQ = r'>'
    PQA = r'\('
    PQC = r'\)'

    #Ignorar
    ignore_newline = r'\n+'

    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
