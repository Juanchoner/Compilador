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

