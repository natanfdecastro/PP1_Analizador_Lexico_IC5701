import sys

from AnalizadorLexico import Escaner

# Comando de ejecucion: python3 Main.py <programa.txt>

# Editar la ruta según computadora que se ejecuta
ruta = "C:/Users/Fabrizio/Documents/GitHub/PP1_Analizador_Lexico_IC5701/src/resources/"

#Abre el archivo del código que se va a procesar.
archivo = open(ruta + sys.argv[1],'r')

#Lee el archivo del código que se va a procesar.
programa = archivo.read()

#Cierra el archivo del código que se va a procesar.
archivo.close()

scanner = Escaner(programa)