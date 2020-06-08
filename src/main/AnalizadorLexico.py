import re  # Importa la biblioteca que maneja regex de Python


class Escaner:

    def __init__(self, programa):

        # Contiene el programa leido del programa.txt
        self.programa = programa

        self.token_palabra_clave = r'abstracto|asertar|booleano|romper|byte|caso|atrapar|caracter|clase|continuar' \
                                 r'|predeterminado|hacer|doble|sino|enum|extender|final|finalmente|flotante|para|si' \
                                 r'|implementa|importar|instanciable|ent|interfaz|largo|nativo|nuevo|nulo|paquete' \
                                 r'|privado|protegido|publico|retornar|corto|estatico|estrictofp|super|cambiar' \
                                 r'|sincronizado|este|arroja|arrojan|transitorio|tratar|vacio|volatil|mientras|Hilera' \
                                 r'|imprimirln|imprimir '
        self.tokenBooleano = r'verdad|falso'
        self.tokenEntero = r'[0-9]+'
        self.tokenIdentificador = r'[A-Za-z0-9_]+'
        self.tokenOperador = r'-|\+|/|\*|\+|='
        self.tokenOperadorLogico = r'==|>=|<=|>|<|&&'
        self.tokenHilera = r'"[A-Za-z0-9]+"'
        self.tokenSimboloEspecial = r',|;|\(|\)|{|}|\[|\]|\.'
        self.tokenError = r'[\S]+'

        # Se crea un regex con todos los posibles tokens para formar la gramatica
        self.gramatica = r'(' + self.token_palabra_clave + ')|(' + self.tokenBooleano + ')|(' \
                         + self.tokenEntero + ')|(' + self.tokenIdentificador + ')|(' \
                         + self.tokenOperador + ')|(' + self.tokenOperadorLogico + ')|(' \
                         + self.tokenHilera + ')|(' + self.tokenSimboloEspecial + ')|(' + self.tokenError + ')'

        self.tokensEncontrados = []
        self.tokensErroneos = []
        self.error = False

        self.buscar_tokens()
        self.mostrar_Tokens()

    def buscar_tokens(self):

        print(self.programa)
        self.gramatica = re.compile(self.gramatica)  # Prepara la gramatica para hacer match

        matches = self.gramatica.finditer(self.programa)

        for match in matches:
            if type(match.group(1)) == str:
                self.tokensEncontrados += [["PALABRA_CLAVE", match.group(1)]]
            elif type(match.group(2)) == str:
                self.tokensEncontrados += [["BOOLEANO", match.group(2)]]
            elif type(match.group(3)) == str:
                self.tokensEncontrados += [["ENTERO", match.group(3)]]
            elif type(match.group(4)) == str:
                self.tokensEncontrados += [["IDENTIFICADOR", match.group(4)]]
            elif type(match.group(5)) == str:
                self.tokensEncontrados += [["OPERADOR", match.group(5)]]
            elif type(match.group(6)) == str:
                self.tokensEncontrados += [["OPERADOR_LOGICO", match.group(6)]]
            elif type(match.group(7)) == str:
                self.tokensEncontrados += [["HILERA", match.group(7)]]
            elif type(match.group(8)) == str:
                self.tokensEncontrados += [["SIMBOLO_ESPECIAL", match.group(8)]]
            elif type(match.group(9)) == str:
                print("ERROR: Token no reconocido" + match.group(9))
                self.error = True

    def mostrar_Tokens(self):

        cuenta = 0
        print("Tokens encontrados: \n")

        for token in self.tokensEncontrados:
            print(str(cuenta) + " " + str(token))
            cuenta += 1
        print()
