#!/usr/bin/python3
"""Allows to write in a file"""


def write_file(filename="", text=""):
    """
    Write in the file.
    """
    with open(filename, "w") as f:
        writing = f.write(text)
        return (writing)
