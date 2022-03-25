'''
Script en python en el cual se generan las intencias de los analizaodres
para así generar una mini-calculadora
'''

import sys
sys.path.insert(0, '../..')

from analizador_lexico import CalculadoraLexer
from analizador_sintactico import CalculadoraParser

if __name__ == '__main__':
    lexer = CalculadoraLexer()
    parser = CalculadoraParser()

    while True:
        try:
            text = input('cal >')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))
