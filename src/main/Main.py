import sys
import os

from AnalizadorLexico import Escaner

# Comando de ejecucion: python3 Main.py <programa.txt>


path = os.getcwd().split("\\")
new_path = ""

for i in range(len(path)-1):
    new_path += path[i] + '/'

new_path += "resources/"

# Editar la ruta según computadora que se ejecuta
archivo = open(new_path + sys.argv[1],'r')

programa = archivo.read()

archivo.close()

scanner = Escaner(programa)