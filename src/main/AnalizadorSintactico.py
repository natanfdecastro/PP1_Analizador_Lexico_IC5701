from ArbolSintaxisAbstracta import *


class AnalizadorSintactico():

    arbol_sintaxis_abstracta = 0
    errores = 0
    tokens_encontrados = []
    cantidad_tokens = 0

    def __init__(self, tokens_encontrados):
      
        self.tokens_encontrados = tokens_encontrados
      
        self.cantidad_tokens = len(tokens_encontrados)

        if self.cantidad_tokens == 0:
      
            print("No hay tokens suficientes para iniciar el analisis")

        self.analizar_sintaxis()


    # Funcion inicial del parseo.
    def analizar_sintaxis(self):

        # Inicia con le primer nodo del árbol (raiz).
        self.arbol_sintaxis_abstracta = Nodo_Raiz("RAIZ", "", [])
  
        puntero_ast = self.arbol_sintaxis_abstracta
  
        indice_actual_tokens_encontrados = 0

        # Inicia con el parseo y análisis de la sintaxis.
        if (self.analizar_sintaxis_programa(0) == True):

        else:
            # Genera error en caso de problemas en el parseo.
            self.generar_error()

    #Funcion para comparar tokens e identificar su respectivo tipo.
    def comparar_tokens(self,tipo_token,indice_actual_tokens_encontrados):

        # Verifica que este dentro del rango de tokens.
        if(indice_actual_tokens_encontrados < self.tokens_len):

            # Verifica si los tipos son iguales.
            if(self.tokens_encontrados[indice_actual_tokens_encontrados][0] == tipo_token):

                return True

        return False

    # Funcion generador del error detectado.
    def generar_error(self):
  
        rastreo = ""
  
        error = "ERROR DE SINTAXIS\n"
  
        rastreo_maximo = 6

        if (self.puntero_error == len(self.tokens_encontrados)):
            error += "ARGUMENTO FALTANTE\n"
  
        self.puntero_error -= 1

        while (self.puntero_error > -1 and rastreo_maximo > -1):
  
            rastreo = self.tokens_encontrados[self.puntero_error][1] + " " + rastreo
  
            self.puntero_error -= 1
  
            rastreo_maximo -= 1
  
        rastreo += "<--"
  
        print(rastreo)
  
        print(error)

    # Función identificadora del puntero donde se encontro el error.
    def calcular_error(self, indice_actual_tokens_encontrados):
  
        if (indice_actual_tokens_encontrados > self.puntero_error):
            self.puntero_error = indice_actual_tokens_encontrados

    
    # Parsea analizando sintacticamente un nodo no terminal de tipo operacion_matematica
    def parsear_operacion_matematica(self, indice_actual_tokens_encontrados):

        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta = Nodo_Operacion_Matematica("OPERACION_MATEMATICA", "OPERACION_MATEMATICA", [])

        if (self.comparar_tokens("INT", indice_actual_tokens_encontrados) or self.comparar_tokens("NOMBRE", indice_actual_tokens_encontrados)):

            subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
    
            indice_actual_tokens_encontrados += 1
    
            while (self.comparar_tokens("OPERADOR", indice_actual_tokens_encontrados)):

                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
    
                indice_actual_tokens_encontrados += 1
    
                if (self.comparar_tokens("INT", indice_actual_tokens_encontrados) or self.comparar_tokens("NOMBRE", indice_actual_tokens_encontrados)):
    
                    subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
    
                    indice_actual_tokens_encontrados += 1
    
                else:
                    calcular_error(indice_actual_tokens_encontrados)
    
                    return [], -1
    
            return subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta, indice_actual_tokens_encontrados
    
        self.calcular_error(indice_actual_tokens_encontrados)
    
        return [], -1


    # Parsea analizando sintacticamente un nodo no terminal de tipo operacion_logica
    def parsear_operacion_logica(self, indice_actual_tokens_encontrados):

        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta = Nodo_Operacion_Logica("OPERACION_LOGICA", "OPERACION_LOGICA", [])
        
        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_operacion_matematica(indice_actual_tokens_encontrados)
        
        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2, nuevo_puntero2 = self.parsear_valor(indice_actual_tokens_encontrados)
        
        if (self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp) or self.comparar_tokens("NOMBRE", indice_actual_tokens_encontrados) or self.validar_parseo(
        
                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2)):
        
            if (self.comparar_tokens("NOMBRE", indice_actual_tokens_encontrados)):
        
                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
        
                indice_actual_tokens_encontrados += 1
        
            elif (self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2)):
        
                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2)
        
                indice_actual_tokens_encontrados = nuevo_puntero2
        
            elif (self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp)):
        
                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp)
        
                indice_actual_tokens_encontrados = nuevo_puntero

        
            if (self.comparar_tokens("OPERADOR_LOGICO", indice_actual_tokens_encontrados)):
                
                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
                
                indice_actual_tokens_encontrados += 1
               
                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp, nuevo_puntero = self.parsear_operacion_matematica(indice_actual_tokens_encontrados)
                
                subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2, nuevo_puntero2 = self.parsear_valor(indice_actual_tokens_encontrados)
                
                if (self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp) or self.comparar_tokens("NOMBRE",
                                                                       indice_actual_tokens_encontrados) or self.validar_parseo(
                
                        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2)):
                
                    if (self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp)):
                
                        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp)
                
                        indice_actual_tokens_encontrados = nuevo_puntero
                
                    elif (self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2)):
                
                        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta_temp2)
                
                        indice_actual_tokens_encontrados = nuevo_puntero2
                
                    else:
                
                        subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
                
                        indice_actual_tokens_encontrados += 1
                
                    return subarbol_sintaxis_abstracta_sintaxis_abstracta_sintaxis_abstracta, indice_actual_tokens_encontrados

        self.calcular_error(indice_actual_tokens_encontrados)
        
        return [], -1


# Parsea analizando sintacticamente un nodo no terminal de tipo si
# de la produccion Declaracion
def parsear_si(self,indice_actual_tokens_encontrados):

    # Valida si la produccion inicia con token de tipo IF
if(self.comparar("SI",indice_actual_tokens_encontrados)):

    subarbol_sintaxis_abstracta_sintaxis_abstracta = self.crear_nodo(indice_actual_tokens_encontrados)

    indice_actual_tokens_encontrados += 1

    # Valida si hay un parentesis izquierdo luego del IF
    if(self.comparar("L_PARENTESIS",indice_actual_tokens_encontrados)):

        indice_actual_tokens_encontrados += 1

        subarbol_sintaxis_abstracta_sintaxis_abstracta_aux,nuevo_puntero = self.parsear_operacion_logica(indice_actual_tokens_encontrados)

        # Hace un nuevo subarbol_sintaxis_abstracta para la sentencia de validacion y lo que contenga
        if(self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)):

            subarbol_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)

            indice_actual_tokens_encontrados = nuevo_puntero

            # Valida si hay un parentesis derecho luego de la sentencia de validacion
            if(self.comparar("R_PARENTESIS",indice_actual_tokens_encontrados)):

                indice_actual_tokens_encontrados += 1

                # Valida si hay una llave izquierda luego del I
                if(self.comparar("L_CORCHETE",indice_actual_tokens_encontrados)):

                        indice_actual_tokens_encontrados += 1

                        subarbol_sintaxis_abstracta_sintaxis_abstracta_aux,nuevo_puntero = self.parsear_accion(indice_actual_tokens_encontrados)

                        # Hace un nuevo subarbol_sintaxis_abstracta para la sentencia de validacion y lo que contenga
                        if(self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)):

                            subarbol_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)

                            indice_actual_tokens_encontrados = nuevo_puntero

                            # Procesa el contenido del if mientras sea TRUE y crea un subarbol_sintaxis_abstracta para ese contenido
                            while(True):

                                subarbol_sintaxis_abstracta_sintaxis_abstracta_aux,nuevo_puntero = self.parsear_accion(indice_actual_tokens_encontrados)

                                if(self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)):

                                    subarbol_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)

                                    indice_actual_tokens_encontrados = nuevo_puntero
                                else:
                                    break

                            # Valida si hay un Corchete derecho luego contenido del IF
                            if(self.comparar("R_CORCHETE",indice_actual_tokens_encontrados)):

                                indice_actual_tokens_encontrados += 1

                                subarbol_sintaxis_abstracta_sintaxis_abstracta_aux,nuevo_puntero = self.parsear_sino(indice_actual_tokens_encontrados)

                                if(self.validar_parseo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)):

                                    subarbol_sintaxis_abstracta_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_sintaxis_abstracta_aux)
                                    indice_actual_tokens_encontrados = nuevo_puntero
                                # Caso que la estructura Sintactica sea bien parseada retorna el nuevo subarbol creado
                                return subarbol_sintaxis_abstracta_sintaxis_abstracta,indice_actual_tokens_encontrados
# Caso que alguna de las validaciones anidades pasadas no sea verdadera presenta el error				
self.calcular_error(indice_actual_tokens_encontrados)								
return [],-1	

def parsear_sino(self,indice_actual_tokens_encontrados):

        # Valida si la produccion continua con token de tipo SINO
        if(self.comparar("SINO",indice_actual_tokens_encontrados)):
            subarbol_sintaxis_abstracta = self.crear_nodo(indice_actual_tokens_encontrados)
            indice_actual_tokens_encontrados += 1
            # Valida si hay parentesis izquierdo luego del token tipo SINO
            if(self.comparar("L_CORCHETE",indice_actual_tokens_encontrados)):
                indice_actual_tokens_encontrados += 1
                subarbol_sintaxis_abstracta_aux,nuevo_puntero = self.parsear_accion(indice_actual_tokens_encontrados)
                # Crea un nuevo subarbol para el contenido del sino
                if(self.validar_parseo(subarbol_sintaxis_abstracta_aux)):
                    subarbol_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_aux)
                    indice_actual_tokens_encontrados = nuevo_puntero
                    # Procesa el contenido del sino mientras sea True
                    while(True):
                        subarbol_sintaxis_abstracta_aux,nuevo_puntero = self.parsear_accion(indice_actual_tokens_encontrados)
                        if(self.validar_parseo(subarbol_sintaxis_abstracta_aux)):
                            subarbol_sintaxis_abstracta.agregar_nodo(subarbol_sintaxis_abstracta_aux)
                            indice_actual_tokens_encontrados = nuevo_puntero
                        else:
                            break
                    # Valida que haya una llave izquierda cerrando el sino
                    if(self.comparar("R_CORCHETE",indice_actual_tokens_encontrados)):
                        indice_actual_tokens_encontrados += 1
                        # Caso que la estructura Sintactica sea bien parseada retorna el nuevo subarbol creado
                        return subarbol_sintaxis_abstracta,indice_actual_tokens_encontrados
        # Caso que alguna de las validaciones anidades pasadas no sea verdadera presenta el error
        self.calcular_error(indice_actual_tokens_encontrados)
        return [],-1



def parsear_DeclVar(self,indice_actual_tokens_encontrados):
        subarbol_sintaxis_abstracta = Nodo_DeclVar("DeclVar","DeclVar",[])
        nuevo_puntero = indice_actual_tokens_encontrados

        # Compara que el token al que apunta concuerde con token TIPO
        if(self.comparar("TIPO",indice_actual_tokens_encontrados)):
            subarbol_sintaxis_abstracta.agregar_nodo(self.crear_nodo(indice_actual_tokens_encontrados))
            indice_actual_tokens_encontrados+=1
            arbol_aux,nuevo_puntero = self.parsear_asignacion(indice_actual_tokens_encontrados)
            # Crea un nuevo subarbol para el contenido de la DeclVar
            if(self.validar_parseo(arbol_aux)):
                indice_actual_tokens_encontrados = nuevo_puntero
                subarbol_sintaxis_abstracta.agregar_nodo(arbol_aux)
                # Valida que haya un token de tipo PUNTO_Y_COMA para finalizar
                # la DeclVar
                if(self.comparar("PUNTO_Y_COMA",indice_actual_tokens_encontrados)):
                        indice_actual_tokens_encontrados += 1
                        return subarbol_sintaxis_abstracta,indice_actual_tokens_encontrados
                # Caso que la estructura Sintactica sea bien parseada retorna el nuevo subarbol creado
                return subarbol_sintaxis_abstracta,indice_actual_tokens_encontrados
        # Caso que alguno de las validaciones anidades pasadas no sea verdadera presenta el error
        self.calcular_error(indice_actual_tokens_encontrados)
        return [],-1


    # Función que valida el parseo de una expresión, ya que si se detecta un error, el árbol automaticamente se
    # vuelve nulo, por lo que retorna True si fue correcto, o False si no.
    def validar_parseo(self, subarbol_sintaxis_abstracta):
        if (subarbol_sintaxis_abstracta == []):
            return False
        return True


    #Función que crea los nodos que se le van añadiendo al AST, según el token que identifica.
    def crear_nodo(self, indice_actual_tokens_encontrados):

        tipo_token = self.tokens_encontrados[indice_actual_tokens_encontrados][0]
        valor_token = self.tokens_encontrados[indice_actual_tokens_encontrados][1]
        nodo = []
        if (tipo_token == "DECLARACION"):
            nodo = Nodo_Declaracion(tipo_token, valor_token, [])
        elif (tipo_token == "TIPO"):
            nodo = Nodo_Tipo(tipo_token, valor_token, [])
        elif (tipo_token == "IDENTIFICADOR"):
            nodo = Nodo_Identificador(tipo_token, valor_token, [])
        elif (tipo_token == "OPERADOR"):
            nodo = Nodo_Operador(tipo_token, valor_token, [])
        elif (tipo_token == "OPERADOR_LOGICO"):
            nodo = Nodo_Operador_Logico(tipo_token, valor_token, [])
        elif (tipo_token == "HILERA"):
            nodo = Nodo_Hilera(tipo_token, valor_token, [])
        elif (tipo_token == "COMA"):
            nodo = Nodo_Coma(tipo_token, str(valor_token), [])
        elif (tipo_token == "PUNTO_Y_COMA"):
            nodo = Nodo_Punto_y_Coma(tipo_token, valor_token, [])
        elif (tipo_token == "L_PARENTESIS"):
            nodo = Nodo_L_Parentesis(tipo_token, valor_token, [])
        elif (tipo_token == "R_PARENTESIS"):
            nodo = Nodo_R_Parentesis(tipo_token, valor_token, [])
        elif (tipo_token == "L_CUADRADO"):
            nodo = Nodo_L_Cuadrado(tipo_token, valor_token, [])
        elif (tipo_token == "R_CUADRADO"):
            nodo = Nodo_R_Cuadrado(tipo_token, valor_token, [])
        elif (tipo_token == "L_CORCHETE"):
            nodo = Nodo_L_Corchete(tipo_token, valor_token, [])
        elif (tipo_token == "R_CORCHETE"):
            nodo = Nodo_R_Corchete(tipo_token, valor_token, [])
        elif (tipo_token == "PUNTO"):
            nodo = Nodo_Punto(tipo_token, valor_token, [])
        elif (tipo_token == "SI"):
            nodo = Nodo_Si(tipo_token, valor_token, [])
        elif (tipo_token == "SINO"):
            nodo = Nodo_Sino(tipo_token, valor_token, [])
        elif (tipo_token == "LISTA_FORMAL"):
            nodo = Nodo_Lista_Formal(tipo_token, valor_token, [])
        elif (tipo_token == "PUBLICO"):
            nodo = Nodo_Publico(tipo_token, valor_token, [])
        return nodo


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

