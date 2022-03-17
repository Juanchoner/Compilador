import ply.yacc as yacc
from main import tokens 

def p_expression_plus(p):
    'expression: expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression: expression MINUS term'
    p[0] = p[1] - p[3]
    
def p_expression_term(p):
    'expression: expression term'
    p[0] = p[1]
    
