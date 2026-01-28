import os

def add(a, b):
    cmd = "echo " + str(a)
    os.system(cmd)
    return a + b

