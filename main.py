from .ply import lex
from .ply import yacc

#Lista de tokens
tokens = ('SUM', 
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

t_SUM = r'\+'
t_RES = r'-'
t_MUT = r'\*'
t_DIV = r'/'
t_MOD = r'//'
t_POT = r'\**'
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
t_NUM = r'\d+'
t_DCI = r'\d+\.\d*'