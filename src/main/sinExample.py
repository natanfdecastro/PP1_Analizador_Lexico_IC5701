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

def p_inicial(p):
   '''
   inicial : programa
   '''
   print(p[1])

def p_programa(p):
   '''
   programa : claseprincipal declclase
   '''
   p[0] = (p[1] , p[2])

def p_claseprincipal(p):
   '''
   claseprincipal : PALABRA_CLAVE PALABRA_CLAVE IDENTIFICADOR L_CORCHETE PALABRA_CLAVE PALABRA_CLAVE PALABRA_CLAVE PALABRA_CLAVE L_PARENTESIS PALABRA_CLAVE L_CUADRADO R_CUADRADO IDENTIFICADOR R_PARENTESIS L_CORCHETE R_CORCHETE R_CORCHETE
   '''
   p[0] = p[1]

def p_declclase(p):
    '''
    declclase : PALABRA_CLAVE IDENTIFICADOR declclaseprima
    '''
    p[0] = (p[1] ,p[2], p[3])

def p_declclaseprima(p):
    '''
    declclaseprima : L_CORCHETE declavar declmetodo R_CORCHETE
                   | PALABRA_CLAVE IDENTIFICADOR L_CORCHETE declavar declmetodo R_CORCHETE
    '''
    p[0] = p[1]

def p_declavar(p):
    '''
    declavar : tipo IDENTIFICADOR PUNTO_Y_COMA
    '''
    p[0] = (p[1], p[2], p[3])

def p_declmetodo(p):
    '''
    declmetodo : PALABRA_CLAVE tipo IDENTIFICADOR L_PARENTESIS listaformal R_PARENTESIS L_CORCHETE declavar declaracion PALABRA_CLAVE expren PUNTO_Y_COMA R_CORCHETE
    '''
    p[0] = ( p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[3])

def p_listaformal(p):
    '''
    listaformal : tipo IDENTIFICADOR restricformal
    '''
    p[0] = p[1] , p[2] , p[3]

def p_restricformal(p):
    '''
    restricformal : COMA tipo IDENTIFICADOR
    '''
    p[0] = p[1], p[2], p[3]

def p_tipo(p):
    '''
    tipo : ENTERO L_CUADRADO R_CUADRADO
        | BOOLEANO
        | ENTERO
        | IDENTIFICADOR
    '''
    p[0] = p[1]

def p_declaracion(p):
    '''
    declaracion : L_CORCHETE declaracion R_CORCHETE
                | PALABRA_CLAVE L_PARENTESIS expren R_PARENTESIS declaracion PALABRA_CLAVE declaracion
                | PALABRA_CLAVE L_PARENTESIS expren R_PARENTESIS declaracion
                | PALABRA_CLAVE L_PARENTESIS expren R_PARENTESIS PUNTO_Y_COMA
                | IDENTIFICADOR OPERADOR expren PUNTO_Y_COMA
                | IDENTIFICADOR L_CUADRADO expren R_CUADRADO OPERADOR expren
    '''
    p[0] = p[1]

def p_expren(p):
    '''
    expren : ENTERO exprenprima
            | IDENTIFICADOR exprenprima
            | PALABRA_CLAVE exprenprima
            | PALABRA_CLAVE PALABRA_CLAVE L_CUADRADO expren R_CUADRADO exprenprima
            | PALABRA_CLAVE IDENTIFICADOR L_PARENTESIS R_PARENTESIS exprenprima
            | expren exprenprima
            | L_PARENTESIS expren R_PARENTESIS exprenprima
    '''
    p[0] = p[1] , p[2]

def p_exprenprima(p):
    '''
    exprenprima :  OPERADOR expren
                | L_CUADRADO expren R_CUADRADO
                | PUNTO PALABRA_CLAVE
                | PUNTO IDENTIFICADOR L_PARENTESIS IDENTIFICADOR R_PARENTESIS
    '''
    p[0] = p[1], p[2]

def p_error(p):
    print(p)
    print("Error sintactico")

parser = yacc.yacc()

while True:
    try:
        s = input('').split(" ")
    except EOFError:
        break
    for i in s:
        parser.parse(i)
