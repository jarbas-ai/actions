import sys
import shutil
#Function erase directory

def rmdir(path):
    shutil.rmtree(path)
    return True

rmdir(sys.argv[1])
