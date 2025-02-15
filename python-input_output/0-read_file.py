#!/usr/bin/python3
"""Module for reading a text file"""


def read_file(filename=""):
    with open(filename, "r") as f:
        contenu = f.read()
    print(contenu)
