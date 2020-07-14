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


    # Método para parsear una declaración de método.
    # indice_actual_tokens_encontrados hace referencia a la posicion actual de la hilera de tokens.
    def parsear_DeclMetodo(self, indice_actual_tokens_encontrados):

        # Hace una condicion para verificar que el primer token encontrado sea el de "publico".
        if(self.comparar("PUBLICO", indice_actual_tokens_encontrados)):
            subarbol_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
            indice_actual_tokens_encontrados += 1
            # Hace una condicion para verificar que el siguiente token encontrado sea el de "tipo".
            if (self.comparar("TIPO", indice_actual_tokens_encontrados)):
                indice_actual_tokens_encontrados += 1
                subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_tipo(indice_actual_tokens_encontrados)
                # Hace una condicion para verificar que el siguiente token encontrado sea el de "iden".
                if (self.comparar("IDEN", indice_actual_tokens_encontrados)):
                    indice_actual_tokens_encontrados += 1
                    # Hace una condicion para verificar que el siguiente token encontrado sea el de "(".
                    if (self.comparar("L_PARENTESIS", indice_actual_tokens_encontrados)):
                        indice_actual_tokens_encontrados += 1
                        # Hace una condicion para verificar que el siguiente token encontrado sea el de "listaFormal".
                        if (self.comparar("LISTA_FORMAL", indice_actual_tokens_encontrados)):
                            indice_actual_tokens_encontrados += 1
                            subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_lista_formal(indice_actual_tokens_encontrados)
                            # Hace una condicion para verificar que el siguiente token encontrado sea el de ")".
                            if (self.comparar("R_PARENTESIS", indice_actual_tokens_encontrados)):
                                indice_actual_tokens_encontrados += 1
                                # Hace una condicion para verificar que el siguiente token encontrado sea el de "{".
                                if (self.comparar("L_CORCHETE", indice_actual_tokens_encontrados)):
                                    indice_actual_tokens_encontrados += 1

                                    subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_decl_var(indice_actual_tokens_encontrados)
                                    # Hace una condicion para verificar que el siguiente token encontrado sea el de "DeclVar".
                                    if (self.comparar_tokens(subarbol_sintaxis_abstracta_temp)):
                                        subarbol_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_temp)
                                        indice_actual_tokens_encontrados = nuevo_puntero

                                        # Hace un ciclo ya que puede haber más de una DeclVar.
                                        while (True):
                                            subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_decl_var(indice_actual_tokens_encontrados)
                                            if (self.comparar_tokens(subarbol_sintaxis_abstracta_temp)):
                                                subarbol_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_temp)
                                                indice_actual_tokens_encontrados = nuevo_puntero
                                            else:
                                                break

                                        subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_accion(indice_actual_tokens_encontrados)
                                        # Hace una condicion para verificar que el siguiente token encontrado sea el de "Declaracion".
                                        if (self.comparar_tokens(subarbol_sintaxis_abstracta_temp)):
                                            subarbol_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_temp)
                                            indice_actual_tokens_encontrados = nuevo_puntero

                                            # Hace un ciclo ya que puede haber más de una Declaración.
                                            while (True):
                                                subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_declaracion(indice_actual_tokens_encontrados)
                                                if (self.comparar_tokens(subarbol_sintaxis_abstracta_temp)):
                                                    subarbol_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_temp)
                                                    indice_actual_tokens_encontrados = nuevo_puntero
                                                else:
                                                    break
                                            # Hace una condicion para verificar que el siguiente token encontrado sea el de "retornar".
                                            if (self.comparar("RETORNAR", indice_actual_tokens_encontrados)):
                                                indice_actual_tokens_encontrados += 1
                                                # Hace una condicion para verificar que el siguiente token encontrado sea el de "expren".
                                                if (self.comparar("EXPREN", indice_actual_tokens_encontrados)):
                                                    indice_actual_tokens_encontrados += 1
                                                    subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_expren(indice_actual_tokens_encontrados)
                                                    # Hace una condicion para verificar que el siguiente token encontrado sea el de ";".
                                                    if (self.comparar("PUNTO_Y_COMA", indice_actual_tokens_encontrados)):
                                                        indice_actual_tokens_encontrados += 1
                                                        # Hace una condicion para verificar que el siguiente token encontrado sea el de "}".
                                                        if (self.comparar("CORCHETE_DERECHO", indice_actual_tokens_encontrados)):
                                                            indice_actual_tokens_encontrados += 1
        # En caso de que no identifique algún token, devolvería error.
        self.calcular_error(indice_actual_tokens_encontrados)
        return [], -1

    # Método para parsear una declaración de método.
    # indice_actual_tokens_encontrados hace referencia a la posicion actual de la hilera de tokens.
    def parsear_RestricFormal(self, indice_actual_tokens_encontrados):

        # Hace una condicion para verificar que el siguiente token encontrado sea el de ",".
        if (self.comparar("COMA", indice_actual_tokens_encontrados)):
            indice_actual_tokens_encontrados += 1
            # Hace una condicion para verificar que el siguiente token encontrado sea el de "Tipo".
            if (self.comparar("TIPO", indice_actual_tokens_encontrados)):
                indice_actual_tokens_encontrados += 1
                subarbol_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_tipo(indice_actual_tokens_encontrados)
                # Hace una condicion para verificar que el siguiente token encontrado sea el de "iden".
                if (self.comparar("IDEN", indice_actual_tokens_encontrados)):
                    indice_actual_tokens_encontrados += 1

        # En caso de que no identifique algún token, devolvería error.
        self.calcular_error(indice_actual_tokens_encontrados)
        return [], -1