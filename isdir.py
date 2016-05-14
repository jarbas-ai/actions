import sys
import os
#Funcao retorna true se a entrada e um diretorio valido

def isdir(path):
    return os.path.isdir(path)

isdir(sys.argv[1])
