import os
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

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
    print("Error en el léxico '%s' " % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'

lexer = lex.lex()

def p_restricformal(p):
    '''
    restricformal : COMA tipo IDENTIFICADOR
    '''
    print("restricformal")
    p[0] = p[1],p[2],p[3]

def p_programa(p):
   '''
   programa : claseprincipal declclase
   '''
   print("programa")
def p_claseprincipal(p):
   '''
   claseprincipal : PALABRA_CLAVE PALABRA_CLAVE IDENTIFICADOR L_CORCHETE PALABRA_CLAVE PALABRA_CLAVE PALABRA_CLAVE PALABRA_CLAVE L_PARENTESIS PALABRA_CLAVE L_CUADRADO R_CUADRADO IDENTIFICADOR R_PARENTESIS L_CORCHETE R_CORCHETE R_CORCHETE
   '''
   print("claseprincipal")
def p_declclase(p):
    '''
    declclase : PALABRA_CLAVE IDENTIFICADOR declclaseprima
    '''
    print("declclase")

def p_declclaseprima1(p):
    '''
    declclaseprima : L_CORCHETE declavar declmetodo R_CORCHETE

    '''
    print("declclaseprima")

def p_declclaseprima2(p):
    '''
    declclaseprima : PALABRA_CLAVE IDENTIFICADOR L_CORCHETE declavar declmetodo R_CORCHETE
    '''
    print("declclaseprima")

def p_declavar(p):
    '''
    declavar : tipo IDENTIFICADOR PUNTO_Y_COMA
    '''
    print("declavar")
def p_declmetodo(p):
    '''
    declmetodo : PALABRA_CLAVE tipo IDENTIFICADOR L_PARENTESIS listaformal R_PARENTESIS L_CORCHETE declavar declaracion PALABRA_CLAVE expren PUNTO_Y_COMA R_CORCHETE
    '''
    print("declmetodo")
def p_listaformal(p):
    '''
    listaformal : tipo IDENTIFICADOR restricformal
    '''
    print("listaformal")

def p_tipo1(p):
    '''
    tipo : ENTERO L_CUADRADO R_CUADRADO
    '''
    print("tipo")

def p_tipo2(p):
    '''
    tipo :  BOOLEANO
    '''
    print("tipo")

def p_tipo3(p):
    '''
    tipo : ENTERO
    '''
    print("tipo")

def p_tipo4(p):
    '''
    tipo : IDENTIFICADOR
    '''
    print("tipo")

def p_declaracion1(p):
    '''
    declaracion : L_CORCHETE declaracion R_CORCHETE
    '''
    print("declaracion")

def p_declaracion2(p):
    '''
    declaracion : PALABRA_CLAVE L_PARENTESIS expren R_PARENTESIS declaracion PALABRA_CLAVE declaracion
    '''
    print("declaracion")

def p_declaracion3(p):
    '''
    declaracion : PALABRA_CLAVE L_PARENTESIS expren R_PARENTESIS declaracion
    '''
    print("declaracion")

def p_declaracion4(p):
    '''
    declaracion : PALABRA_CLAVE L_PARENTESIS expren R_PARENTESIS PUNTO_Y_COMA
    '''
    print("declaracion")

def p_declaracion5(p):
    '''
    declaracion : IDENTIFICADOR OPERADOR expren PUNTO_Y_COMA
    '''
    print("declaracion")


def p_declaracion6(p):
    '''
    declaracion : IDENTIFICADOR L_CUADRADO expren R_CUADRADO OPERADOR expren
    '''
    print("declaracion")

def p_declaracion7(p):
    '''
    declaracion :
    '''
    print("declaracion")

def p_expren1(p):
    '''
    expren : ENTERO exprenprima
    '''
    print("expren")

def p_expren2(p):
    '''
    expren : IDENTIFICADOR exprenprima
    '''
    print("expren")

def p_expren3(p):
    '''
    expren : PALABRA_CLAVE exprenprima
    '''
    print("expren")

def p_expren4(p):
    '''
    expren : PALABRA_CLAVE PALABRA_CLAVE L_CUADRADO expren R_CUADRADO exprenprima
    '''
    print("expren")

def p_expren5(p):
    '''
    expren : PALABRA_CLAVE IDENTIFICADOR L_PARENTESIS R_PARENTESIS exprenprima
    '''
    print("expren")

def p_expren6(p):
    '''
    expren : expren exprenprima
    '''
    print("expren")

def p_expren7(p):
    '''
    expren : L_PARENTESIS expren R_PARENTESIS exprenprima
    '''
    print("expren")

def p_expren8(p):
    '''
    expren :
    '''
    print("expren")

def p_exprenprima1(p):
    '''
    exprenprima :  OPERADOR expren
    '''
    print("exprenprima")

def p_exprenprima2(p):
    '''
    exprenprima :  L_CUADRADO expren R_CUADRADO
    '''
    print("exprenprima")

def p_exprenprima3(p):
    '''
    exprenprima : PUNTO PALABRA_CLAVE
    '''
    print("exprenprima")

def p_exprenprima4(p):
    '''
    exprenprima : PUNTO IDENTIFICADOR L_PARENTESIS IDENTIFICADOR R_PARENTESIS
    '''
    print("exprenprima")

def p_exprenprima5(p):
    '''
    exprenprima :
    '''
    print("exprenprima")

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_error(p):
    print("Error sintactico", p)
    print("Error en la línea: " + str(p.lineno))

path = os.getcwd().split("\\")
new_path = ""
for i in range(len(path)-1):
    new_path += path[i] + '/'
new_path += "resources/"
archivo = open(new_path + sys.argv[1],'r')
programa = archivo.read()

parser = yacc.yacc()
print(parser.parse(", entero akjsbd"))
print(parser.parse(", booleano variable1"))
print(parser.parse(", hilera variable2"))
print(parser.parse(", identificadorDePrueba variable3"))
resultado1 = parser.parse(programa)
