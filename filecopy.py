# -*- CODING: UTF-8 -*-
import sys
import shutil
#Funcao copiar arquivo para pasta


def filecopy(absfilepath, destinationpath):
    shutil.copyfile(absfilepath, destinationpath)
    return True

in1 = sys.argv[1]
in2 = sys.argv[2]

filecopy(in1, in2)
