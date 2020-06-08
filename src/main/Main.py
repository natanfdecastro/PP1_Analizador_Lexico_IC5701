import sys

from AnalizadorLexico import Escaner

# Comando de ejecucion: python3 Main.py <programa.txt>

# Editar la ruta según computadora que se ejecuta
ruta = "C:/Users/windows10/Documents/TEC/I Semestre - 2020/Compiladores E Intérpretes/PP1_Analizador_Lexico_IC5701/src/resources/"

archivo = open(ruta + sys.argv[1],'r')

programa = archivo.read()

archivo.close()

scanner = Escaner(programa)