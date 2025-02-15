#!/usr/bin/python3
"""Allows to append a str in a  file."""


def append_write(filename="", text=""):
    """Add a string at the end of a UTF8 text file."""
    with open(filename, "a") as f:
        app = f.write(text)
        return (app)
