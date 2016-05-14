# -*- CODING: UTF-8 -*-
import shutil
#Função mover arquivo para pasta

def filemove(absfilepath, destinationpath):
    shutil.copyfile(absfilepath, destinationpath)
    return True
