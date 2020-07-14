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

        def generar_error(self):
            rastreo = ""
            error = "Sintaxis Invalida\n"
            rastreo_maximo = 6

            if (self.puntero_error == len(self.tokens_encontrados)):
                error += "Hace falta un argumento al final\n"
            self.puntero_error -= 1

            while (self.puntero_error > -1 and rastreo_maximo > -1):
                rastreo = self.tokens_encontrados[self.puntero_error][1] + " " + rastreo
                self.puntero_error -= 1
                rastreo_maximo -= 1
            rastreo += "\x1b[1;31m <--- \x1b[1;37m"
            print(rastreo)
            print(error)

        def calcular_error(self, puntero_token):
            if (puntero_token > self.puntero_error):
                self.puntero_error = puntero_token

        def parsear_operacion_matematica(self, puntero_token):

            subarbol = Nodo_Operacion_Matematica("OPERACION_MATEMATICA", "OPERACION_MATEMATICA", [])

            if (self.comparar("INT", puntero_token) or self.comparar("NOMBRE", puntero_token)):

                subarbol.agregar_nodo(self.crear_nodo(puntero_token))
                puntero_token += 1
                while (self.comparar("OPERADOR", puntero_token)):

                    subarbol.agregar_nodo(self.crear_nodo(puntero_token))
                    puntero_token += 1
                    if (self.comparar("INT", puntero_token) or self.comparar("NOMBRE", puntero_token)):
                        subarbol.agregar_nodo(self.crear_nodo(puntero_token))
                        puntero_token += 1
                    else:
                        calcular_error(puntero_token)
                        return [], -1
                return subarbol, puntero_token
            self.calcular_error(puntero_token)
            return [], -1

        def parsear_operacion_logica(self, puntero_token):
            subarbol = Nodo_Operacion_Logica("OPERACION_LOGICA", "OPERACION_LOGICA", [])
            subarbol_aux, nuevo_puntero = self.parsear_operacion_matematica(puntero_token)
            subarbol_aux2, nuevo_puntero2 = self.parsear_valor(puntero_token)
            if (self.validar_parseo(subarbol_aux) or self.comparar("NOMBRE", puntero_token) or self.validar_parseo(
                    subarbol_aux2)):
                if (self.comparar("NOMBRE", puntero_token)):
                    subarbol.agregar_nodo(self.crear_nodo(puntero_token))
                    puntero_token += 1
                elif (self.validar_parseo(subarbol_aux2)):
                    subarbol.agregar_nodo(subarbol_aux2)
                    puntero_token = nuevo_puntero2
                elif (self.validar_parseo(subarbol_aux)):
                    subarbol.agregar_nodo(subarbol_aux)
                    puntero_token = nuevo_puntero

                if (self.comparar("OPERADOR_LOGICO", puntero_token)):
                    subarbol.agregar_nodo(self.crear_nodo(puntero_token))
                    puntero_token += 1
                    subarbol_aux, nuevo_puntero = self.parsear_operacion_matematica(puntero_token)
                    subarbol_aux2, nuevo_puntero2 = self.parsear_valor(puntero_token)
                    if (self.validar_parseo(subarbol_aux) or self.comparar("NOMBRE",
                                                                           puntero_token) or self.validar_parseo(
                            subarbol_aux2)):
                        if (self.validar_parseo(subarbol_aux)):
                            subarbol.agregar_nodo(subarbol_aux)
                            puntero_token = nuevo_puntero
                        elif (self.validar_parseo(subarbol_aux2)):
                            subarbol.agregar_nodo(subarbol_aux2)
                            puntero_token = nuevo_puntero2
                        else:
                            subarbol.agregar_nodo(self.crear_nodo(puntero_token))
                            puntero_token += 1
                        return subarbol, puntero_token

            self.calcular_error(puntero_token)
            return [], -1

        def imprimir_AST(self):
            print(self.AST.hijos[0].hijos[0].tipo)

            lista = [self.AST]
            arbol_string = ""

            while (lista != []):

                arbol_string += lista[0].tipo + "\n---> "

                for hijo in lista[0].hijos:
                    arbol_string += hijo.tipo + " "
                    lista += [hijo]

                arbol_string += "\n\n";
                lista = lista[1:]

            print("Arbol AST:\n")
            print(arbol_string)

