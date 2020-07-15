import os
import re  # Importa la biblioteca que maneja regex de Python

import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'PALABRA_CLAVE',
    'BOOLEANO',
    'ENTERO',
    'IDENTIFICADOR',
    'OPERADOR',
    'OPERADOR_LOGICO',
    'COMA',
    'HILERA',
    'PUNTO_Y_COMA',
    'L_PARENTESIS',
    'R_PARENTESIS',
    'R_CUADRADO',
    'L_CUADRADO',
    'L_CORCHETE',
    'R_CORCHETE',
    'PUNTO',
    'ESPACIO',
]

def t_PALABRA_CLAVE(t):
    r' booleano|caracter|clase|este|vacio|estatico|Sistema' \
    r'|sino|extiende|si|salida' \
    r'|ent|nuevo' \
    r'|publico|retornar' \
    r'|mientras|Hilera' \
    r'|imprimirln|imprimir'
    t.type = "PALABRA_CLAVE"
    return t

def t_BOOLEANO(t):
    r'verdad|falso'
    t.type = 'BOOLEANO'
    return t

def t_ENTERO(t):
    r'[0-9]+'
    t.type = 'ENTERO'
    return t

def t_IDENTIFICADOR(t):
    r'[A-Za-z0-9_]+'
    t.type = 'IDENTIFICADOR'
    return t

def t_OPERADOR(t):
    r'-|\+|/|\*|\+|='
    t.type = 'OPERADOR'
    return t
'''
def t_OPERADOR_LOGICO(t):
    r'==|>=|<=|>|<|&&'
    t.type = 'OPERADOR_lOGICO'
    return t
'''
def t_HILERA(t):
    r'"[A-Za-z0-9]+"'
    t.type = 'HILERA'
    return t

def t_COMA(t):
    r','
    t.type = 'COMA'
    return t

def t_LPARENTESIS(t):
    r'\('
    t.type = 'L_PARENTESIS'
    return t

def t_RPARENTESIS(t):
    r'\)'
    t.type = 'R_PARENTESIS'
    return t

def t_LCORCHETE(t):
    r'{'
    t.type = 'L_CORCHETE'
    return t

def t_RCORCHETE(t):
    r'}'
    t.type = 'R_CORCHETE'
    return t

def t_LCUADRADO(t):
    r'\['
    t.type = 'L_CUADRADO'
    return t

def t_RCUADRADO(t):
    r'\]'
    t.type = 'R_CUADRADO'
    return t

def t_PUNTO(t):
    r'\.'
    t.type = 'PUNTO'
    return t

def t_PUNTO_Y_COMA(t):
    r'\;'
    t.type = 'PUNTO_Y_COMA'
    return t

def t_error(t):
    print("Error en el léxico")
    print(t)
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input("")
while(True):
    tok = lexer.token()
    if not tok:
        break
    print(tok)

