import os

def add(a, b):
    cmd = "echo " + a
    os.system(cmd)
    return a + b

