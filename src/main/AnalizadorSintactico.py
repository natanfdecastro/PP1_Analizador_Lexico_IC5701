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


    def parsear_DeclMetodo(self, puntero_token):

        if(self.comparar("PUBLICO", puntero_token)):
            subarbol.agregar_nodo(self.crear_nodo(puntero_token))
            puntero_token += 1
            if (self.comparar("TIPO", puntero_token)):
                puntero_token += 1
                arbol_aux, nuevo_puntero = self.parsear_tipo(puntero_token)
                if (self.comparar("IDEN", puntero_token)):
                    puntero_token += 1
                    if (self.comparar("PAREN_IZQUIERDO", puntero_token)):
                        puntero_token += 1
                        if (self.comparar("LISTA_FORMAL", puntero_token)):
                            puntero_token += 1
                            arbol_aux, nuevo_puntero = self.parsear_lista_formal(puntero_token)
                            if (self.comparar("PAREN_DERECHO", puntero_token)):
                                puntero_token += 1
                                if (self.comparar("CORCHETE_IZQUIERDO", puntero_token)):
                                    puntero_token += 1

                                    subarbol_aux, nuevo_puntero = self.parsear_accion(puntero_token)
                                    if (self.validar_parseo(subarbol_aux)):
                                        subarbol.agregar_nodo(subarbol_aux)
                                        puntero_token = nuevo_puntero

                                        while (True):
                                            subarbol_aux, nuevo_puntero = self.parsear_decl_var(puntero_token)
                                            if (self.validar_parseo(subarbol_aux)):
                                                subarbol.agregar_nodo(subarbol_aux)
                                                puntero_token = nuevo_puntero
                                            else:
                                                break

                                        subarbol_aux, nuevo_puntero = self.parsear_accion(puntero_token)
                                        if (self.validar_parseo(subarbol_aux)):
                                            subarbol.agregar_nodo(subarbol_aux)
                                            puntero_token = nuevo_puntero

                                            while (True):
                                                subarbol_aux, nuevo_puntero = self.parsear_declaracion(puntero_token)
                                                if (self.validar_parseo(subarbol_aux)):
                                                    subarbol.agregar_nodo(subarbol_aux)
                                                    puntero_token = nuevo_puntero
                                                else:
                                                    break

                                            if (self.comparar("RETORNAR", puntero_token)):
                                                puntero_token += 1
                                                if (self.comparar("EXPREN", puntero_token)):
                                                    puntero_token += 1
                                                    arbol_aux, nuevo_puntero = self.parsear_expren(puntero_token)
                                                    if (self.comparar("PUNTO_Y_COMA", puntero_token)):
                                                        puntero_token += 1
                                                        if (self.comparar("CORCHETE_DERECHO", puntero_token)):
                                                            puntero_token += 1
        self.calcular_error(puntero_token)
        return [], -1