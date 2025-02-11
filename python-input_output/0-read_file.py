#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r") as f:
        contenu = f.read()
    print(contenu)
    