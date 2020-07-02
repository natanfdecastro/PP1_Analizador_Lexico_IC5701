class AnalizadorSintactico():

    arbol_sintactico = 0
    errores = 0
    tokens_encontrados = []
    cantidad_tokens = 0

    def __init__(self, tokens_encontrados):

        self.tokens_encontrados = tokens_encontrados
        self.cantidad_tokens = len(tokens_encontrados)

        if cantidad_tokens == 0:
            print("No hay tokens suficientes para iniciar el analisis")

        self.analizar()

        def analizar(self):
            self.arbol_sintactico = Nodo_Programa("PROGRAMA", "", [])
            puntero_ast = self.arbol_sintactico
            puntero_token = 0
            if (self.analizar_programa(0) == True):
                checker = Checker(self.arbol_sintactico)
                informe = checker.checkear()
                if (type(informe) != str):  # no hay errores de tipos
                    return
                else:
                    print(informe)
            else:
                self.generar_error()





