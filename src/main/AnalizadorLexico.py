import re  # Importa la biblioteca que maneja regex de Python

class Escaner:

    def __init__(self, programa):

        '''
        Descripcion: Función inicial de la clase.
        Entradas: Una instancia de la clase, un string con el código de Java Tropicalizado al Español.
        Salidas: Ninguna.
        Restricciones: String de entrada no debe de ser nulo.
        '''

        # Contiene el programa leido del programa.txt
        self.programa = programa

        # Contiene los identificadores de las palabras clave del Java Tropicalizado al Español.
        self.token_palabra_clave = r' booleano|caracter|clase|este|vacio|estatico|Sistema' \
                                 r'|sino|extiende|si|salida' \
                                 r'|ent|nuevo' \
                                 r'|publico|retornar' \
                                 r'|mientras|Hilera' \
                                 r'|imprimirln|imprimir '
        self.token_booleano = r'verdad|falso'
        self.token_entero = r'[0-9]+'
        self.token_identificador = r'[A-Za-z0-9_]+'
        self.token_operador = r'-|\+|/|\*|\+|='
        self.token_operador_logico = r'==|>=|<=|>|<|&&'
        self.token_hilera = r'"[A-Za-z0-9]+"'
        self.token_simbolo_especial = r',|;|\(|\)|{|}|\[|\]|\.'
        self.token_error = r'[\S]+'

        # Se crea un regex con todos los posibles tokens para formar la gramatica
        self.gramatica = r'(' + self.token_palabra_clave + ')|(' + self.token_booleano + ')|(' \
                         + self.token_entero + ')|(' + self.token_identificador + ')|(' \
                         + self.token_operador + ')|(' + self.token_operador_logico + ')|(' \
                         + self.token_hilera + ')|(' + self.token_simbolo_especial + ')|(' + self.token_error + ')'

        self.tokens_encontrados = []
        self.tokens_erroneos = []
        self.error = False

        self.buscar_tokens()
        self.mostrar_Tokens()

    def buscar_tokens(self):

        '''
        Descripcion: Busca e identifica los tokens del código entrante.
        Entradas: Una instancia de la clase.
        Salidas: Ninguna.
        Restricciones: Ninguna.
        '''

        # Imprime el programa ingresado.
        print(self.programa)
        # Prepara la gramatica para hacer match
        self.gramatica = re.compile(self.gramatica)

        matches = self.gramatica.finditer(self.programa)

        # Recorre los matches encontrados para asignarles su respectivo tipo.
        for match in matches:
            if type(match.group(1)) == str:
                self.tokens_encontrados += [["PALABRA_CLAVE", match.group(1)]]
            elif type(match.group(2)) == str:
                self.tokens_encontrados += [["BOOLEANO", match.group(2)]]
            elif type(match.group(3)) == str:
                self.tokens_encontrados += [["ENTERO", match.group(3)]]
            elif type(match.group(4)) == str:
                self.tokens_encontrados += [["IDENTIFICADOR", match.group(4)]]
            elif type(match.group(5)) == str:
                self.tokens_encontrados += [["OPERADOR", match.group(5)]]
            elif type(match.group(6)) == str:
                self.tokens_encontrados += [["OPERADOR_LOGICO", match.group(6)]]
            elif type(match.group(7)) == str:
                self.tokens_encontrados += [["HILERA", match.group(7)]]
            elif type(match.group(8)) == str:
                self.tokens_encontrados += [["SIMBOLO_ESPECIAL", match.group(8)]]
            elif type(match.group(9)) == str:
                print("ERROR: Token no reconocido" + match.group(9))
                self.error = True

    def mostrar_Tokens(self):

        '''
        Descripcion: Muestra los tokens con su respectivo tipo previamente identificado.
        Entradas: Una instancia de la clase.
        Salidas: Ninguna.
        Restricciones: Ninguna.
        '''

        cuenta = 0
        print("Tokens encontrados: \n")

        for token in self.tokens_encontrados:
            print(str(cuenta) + " " + str(token))
            cuenta += 1
        print()