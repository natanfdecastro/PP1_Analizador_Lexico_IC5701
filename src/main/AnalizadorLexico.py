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
        self.token_coma = r','
        self.token_punto_y_coma = r';'
        self.token_Lparentesis = r'\('
        self.token_Rparentesis = r'\)'
        self.token_Lcorchete = r'{'
        self.token_Rcorchete = r'}'
        self.token_Lcuadrado = r'\['
        self.token_Rcuadrado = r'\]'
        self.token_punto = r'\.'
        self.token_error = r'[\S]+'

        # Se crea un regex con todos los posibles tokens para formar la gramatica
        self.gramatica = r'(' + self.token_palabra_clave + ')|(' + self.token_booleano + ')|(' \
                         + self.token_entero + ')|(' + self.token_identificador + ')|(' \
                         + self.token_operador + ')|(' + self.token_operador_logico + ')|(' \
                         + self.token_hilera + ')|(' + self.token_coma + ')|(' + self.token_punto_y_coma + ')|(' \
                         + self.token_Lparentesis + ')|(' + self.token_Rparentesis + ')|(' \
                         + self.token_Rcuadrado + ')|(' + self.token_Lcuadrado + ')|(' \
                         + self.token_Lcorchete + ')|(' + self.token_Rcorchete + ')|(' \
                         + self.token_punto + ')|(' + self.token_error + ')'

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
                self.tokens_encontrados += [["COMA", match.group(8)]]
            elif type(match.group(9)) == str:
                self.tokens_encontrados += [["PUNTO_Y_COMA", match.group(9)]]
            elif type(match.group(10)) == str:
                self.tokens_encontrados += [["L_PARENTESIS", match.group(10)]]
            elif type(match.group(11)) == str:
                self.tokens_encontrados += [["R_PARENTESIS", match.group(11)]]
            elif type(match.group(12)) == str:
                self.tokens_encontrados += [["R_CUADRADO", match.group(12)]]
            elif type(match.group(13)) == str:
                self.tokens_encontrados += [["L_CUADRADO", match.group(13)]]
            elif type(match.group(14)) == str:
                self.tokens_encontrados += [["L_CORCHETE", match.group(14)]]
            elif type(match.group(15)) == str:
                self.tokens_encontrados += [["R_CORCHETE", match.group(15)]]
            elif type(match.group(16)) == str:
                self.tokens_encontrados += [["PUNTO", match.group(16)]]
            elif type(match.group(17)) == str:
                print("ERROR: Token no reconocido" + match.group(17))
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