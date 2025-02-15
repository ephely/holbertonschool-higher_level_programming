#!/usr/bin/python3
"""Module for reading a text file"""


def read_file(filename=""):
    """
    Read the file.
    """
    with open(filename, encoding="utf-8") as f:
        contenu = f.read()
    print(contenu)
