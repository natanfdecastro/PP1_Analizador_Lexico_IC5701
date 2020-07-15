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
]

def t_PALABRA_CLAVE(t):
    r' booleano|caracter|clase|este|vacio|estatico|Sistema' \
    r'|sino|extiende|si|salida' \
    r'|ent|nuevo' \
    r'|publico|retornar' \
    r'|mientras|Hilera' \
    r'|imprimirln|imprimir|Sistema.salida.imprimirnl '
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

def t_OPERADOR_LOGICO(t):
    r'==|>=|<=|>|<|&&'
    t.type = 'OPERADOR_lOGICO'
    return t

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

def t_error(t):
    print("Error en el léxico")
    t.lexer.skip(1)

lexer = lex.lex()

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
    declclase : PALABRACLAVE IDENTIFICADOR declclaseprima
    '''
    p[0] = (p[1] ,p[2], p[3])

def p_declclaseprima(p):
    '''
    declclaseprima : L_CORCHETE declavar declmetodo R_CORCHETE
                   | PALABRA_CLAVE IDENTIFICADOR L_CORCHETE declavar declametodo R_CORCHETE
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
    tipo : ent L_CUADRADO R_CUADRADO
        | booleano
        | ent
        | iden
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
            | PALABRA_CLAVE exprenprima
            | PALABRA_CLAVE exprenprima
            | IDENTIFICADOR exprenprima
            | PALABRA_CLAVE exprenprima
            | PALABRA_CLAVE PALABRA_CLAVE L_CUADRADO expren R_CUADRADO exprenprima
            | PALABRA_CLAVE iden L_PARENTESIS R_PARENTESIS exprenprima
            | expren exprenprima
            | L_PARENTESIS expren R_PARENTESIS exprenprima
    '''
    p[0] = p[1] , p[2]

def p_exprenprima(p):
    '''
    exprenprima :  OPERADOR expren exprenprima
                | [expren] exprenprima
                | PUNTO PALABRACLAVE expreprima
                | PUNTO IDENTIFICADOR L_PARENTESIS listaexp R_PARENTESIS exprenprima
    '''
    p[0] = p[1],p[2]

def p_restricexp(p):
    '''
    restricexp : COMA expren
    '''
    p[0] = p[1] , p [2]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)