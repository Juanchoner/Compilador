import ply.lex as lex
import read_file

#ACTIVIDAD A2
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
        'DCI'
        )

#Expresiones regulares
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

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.value = str(t.value)
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

#cadena = input('Ingrese cadena a evaluar: ')
cadena = read_file.read_text()

lexer.input(cadena)

for token in lexer:
        print(token)
