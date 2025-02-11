#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a") as f:
        app = f.write(text)
        return (app)
