'''
Analizador semantico
Script en python el cual verifique que las palabras esten bien estructuradas
'''
import ply.yacc as yacc
from main import tokens

precedence = (
    ('left','SUM','RES'),
    ('left','MUT','DIV'),
    )

names = { }

def p_statement_assign(t):
    'statement : ID ASG expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression SUM expression
                  | expression RES expression
                  | expression MUT expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression POT expression
                  | expression MRQ expression
                  | expression MYQ expression
                  | expression MRI expression
                  | expression MYI expression
                  | expression COM expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[2] == '%': t[0] = t[1] % t[3]
    elif t[2] == '**': t[0] = t[1] ** t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '>': t[0] = t[1] > t[3]
    elif t[2] == '<=': t[0] = t[1] <= t[3]
    elif t[2] == '>=': t[0] = t[1] >= t[3]
    elif t[2] == '==': t[0] = t[1] == t[3]

def p_expression_group(t):
    'expression : PQA expression PQC'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUM'
    t[0] = t[1]

def p_expression_name(t):
    'expression : ID'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print(f"No se ha definido: {t[1]}")
        t[0] = 0

def p_error(t):
    print(f'Error de sintaxis: {t[1]}')

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    parser.parse(s)
