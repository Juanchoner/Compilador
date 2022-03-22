'''
Analizador léxico
Script en pyrhon el cual analiza un texto de entrada y verifica si se encuentra 
en el lenguaje.
'''
import ply.lex as lex
import read_file

#Palabras reservadas
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'func' : 'FUNCTION',
    'class' : 'CLASS',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'return': "RETURN",
    'this' : "THIS"
}

#Lista de tokens
tokens = (
        'ID',
        'SUM', 
        'RES',
        'DIV',
        'MUT',
        'MOD',
        'POT',
        'ASG',
        'COM',
        'DIF',
        'MRQ',
        'MYQ',
        'MRI',
        'MYI',
        'PQA',
        'PQC',
        'LQA',
        'LQC',
        'CQA',
        'CQC',
        'CDT',
        'NUM',
        'DCI',
        'CMM',
        'DOT'
        )

tokens = list(tokens) + list(reserved.values())
 
t_SUM = r'\+'
t_RES = r'\-'
t_MUT = r'\*'
t_DIV = r'/'
t_MOD = r'//'
t_POT = r'\*\*'
t_ASG = r'='
t_COM = r'=='
t_DIF = r'!='
t_MRQ = r'<'
t_MYQ = r'>'
t_MRI = r'<='
t_MYI = r'>='
t_PQA = r'\('
t_PQC = r'\)'
t_LQA = r'\{'
t_LQC = r'\}'
t_CQA = r'\['
t_CQC = r'\]'
t_CMM = r','
t_DOT = r'\.'
t_ignore_COMMENT = r'\#.*'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CDT(t):
    r''' '.*' | ".*" '''
    t.value = str(t.value)
    return t

def t_DCI(t):
   r'\d*\.\d+'
   t.value = float(t.value)
   return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caracter erroneo: '%s'" % t.value[0])
    t.lexer.skip(1)

#Ejecucion del analizador lexico
lexer = lex.lex()

if __name__ == '__main__':
    text = read_file.read_text()

    lexer.input(text)

    for token in lexer:
        print(token)
