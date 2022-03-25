'''
Script en python en el cual, se crea la clase de CalculadoraParser para relizar
el analisis sintactico de la mini-calculadora
'''

from sly import Parser
from analizador_lexico import CalculadoraLexer

class CalculadoraParser(Parser):
    cal_lex = CalculadoraLexer()
    tokens = cal_lex.tokens

    def __init__(self):
        self.names = { }

    @_('ID ASG expr')
    def statement(self, p):
        self.names[p.ID] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('CDT')
    def factor(self, p):
        return str(p.CDT)

    @_('term { SUM|RES term }')
    def expr(self, p):
        lval = p.term0
        for op, rval in p[1]:
            if op == '+':
                lval = lval + rval
            elif op == '-':
                lval = lval - rval
        return lval

    @_('factor { MUT|DIV|POT|MOD|COM|DIF|MRQ|MYQ|MRI|MYI factor }')
    def term(self, p):
        lval = p.factor0
        for op, rval in p[1]:
            if op == '*':
                lval = lval * rval
            elif op == '/':
                lval = lval / rval
            elif op == '**':
                lval = lval ** rval
            elif op == '%':
                lval = lval % rval
            elif op == '==':
                lval = lval == rval
            elif op == '!=':
                lval = lval != rval
            elif op == '<':
                lval = lval < rval
            elif op == '>':
                lval = lval > rval
            elif op == '<=':
                lval = lval <= rval
            elif op == '>=':
                lval = lval >= rval
        return lval

    @_('RES factor')
    def factor(self, p):
        return -p.factor

    @_('PQA expr PQC')
    def factor(self, p):
        return p.expr

    @_('DCI')
    def factor(self, p):
        return float(p.DCI)

    @_('NUM')
    def factor(self, p):
        return int(p.NUM)

    @_('ID')
    def factor(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print(f'Undefined name {p.ID!r}')
            return 0
