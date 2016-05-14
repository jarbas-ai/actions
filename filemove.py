# -*- CODING: UTF-8 -*-
import sys
import shutil
#Função mover arquivo para pasta


def filemove(absfilepath, destinationpath):
    shutil.move(absfilepath, destinationpath)
    return True

in1 = sys.argv[1]
in2 = sys.argv[2]

filemove(in1, in2)
