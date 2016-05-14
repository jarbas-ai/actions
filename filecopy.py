# -*- CODING: UTF-8 -*-
import sys
import shutil
#Função copiar arquivo para pasta


def filemove(absfilepath, destinationpath):
    shutil.copyfile(absfilepath, destinationpath)
    return True

in1 = sys.argv[1]
in2 = sys.argv[2]

filemove(in1, in2)
