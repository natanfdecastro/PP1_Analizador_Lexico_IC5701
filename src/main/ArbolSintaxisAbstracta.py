'''
Los requerimientos básicos, en el AST, incluyen los siguientes:

    - Los tipos de nodo deben ser preservados, también como la localización de cada declaración en el código fuente.
    - El orden de las declaraciones ejecutables.
    - Los componentes izquierdos y derechos de las operaciones binarias tienen que ser guardadas e identificadas correctamente.
    - Los identificadores y sus valores asignados tienen que ser guardados para las instrucciones de asignación.
'''

class NodoAST:

    tipo_nodo_ast = 0  	# Almacena el tipo de nodo terminal o no terminal
    valor_nodo_ast = 0 	# Almacena el valor asociado al nodo terminal o no terminal Ej: 5 (ent), if
    hijos_nodo_ast = [] # El subarbol asociado al nodo terminal o no terminal

    # Constructor
    def __init__(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast):
 
        self.tipo_nodo_ast = tipo_nodo_ast
 
        self.valor_nodo_ast = valor_nodo_ast
 
        self.hijos_nodo_ast = hijos_nodo_ast

    # Insertar hijos en el nodo
    def agregar_nodo(self, nuevo_nodo_hijo):
 
        self.hijos_nodo_ast += [nuevo_nodo_hijo]

class Nodo_Raiz:

	# Constructor
    def init(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast):
 
        NodoAST.__init__(self, tipo_nodo_ast, valor_nodo_ast, hijos)

    # Determinar correctitud y jerarquia de sintaxis en el AST
    # mediante el patrón de diseño Visitor
    def verificar_correctitud(self, verificador):
 
        return verificador.visitar_nodo_raiz(self)

class Nodo_DeclVar(Nodo):

	# Constructor
	def init(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast):
		
		NodoAST.__init__(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast)
	
	# Determinar correctitud y jerarquia de sintaxis en el AST
	# mediante el patrón de diseño Visitor
	def verificar_correctitud(self, verificador):

		return verificador.visitar_nodo_declvar(self)

class Nodo_Si(Nodo):

	# Constructor
	def init(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast):
		
		NodoAST.__init__(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast)
	
	# Determinar correctitud y jerarquia de sintaxis en el AST
	# mediante el patrón de diseño Visitor
	def verificar_correctitud(self, verificador):

		return verificador.visitar_nodo_si(self)

class Nodo_Sino(Nodo):

	# Constructor
	def init(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast):
		
		NodoAST.__init__(self, tipo_nodo_ast, valor_nodo_ast, hijos_nodo_ast)
	
	# Determinar correctitud y jerarquia de sintaxis en el AST
	# mediante el patrón de diseño Visitor
	def verificar_correctitud(self, verificador):

		return verificador.visitar_nodo_sino(self)





