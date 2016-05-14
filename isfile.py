import sys
import os
#Funcao retorna true se a entrada e um arquivo valido

def isfile(path):
    return os.path.isfile(path)

isfile(sys.argv[1])
