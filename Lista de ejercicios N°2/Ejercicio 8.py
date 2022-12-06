#Definir una función que imprima los argumentos ingresados desde linea de comandos
#Nota: Usar import sys.argv => *args

import sys

def Argumentos(*args):
    for arg in args:
        print(arg)

Argumentos(sys.argv)

