from AnalizadorLexico import Escaner

# Comando de ejecucion: python3 Main.py <programa.txt>

archivo = open("programa.txt")

programa = archivo.read()

archivo.close()

scanner = Escaner(programa)