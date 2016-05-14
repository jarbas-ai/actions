import sys
import os
#Function erase file

def filerm(path):
    os.remove(path)
    return True

filerm(sys.argv[1])
