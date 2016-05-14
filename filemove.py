# -*- CODING: UTF-8 -*-
import shutil
#Função mover arquivo para pasta

def filemove(absfilepath, destinationpath):
    shutil.move(absfilepath, destinationpath)
    return True
