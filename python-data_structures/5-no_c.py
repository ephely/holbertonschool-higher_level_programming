#!/usr/bin/python3
def no_c(my_string):
    chars = list(my_string)
    for char in chars:
        if char == 'c' or char == 'C':
            chars.remove(char)
    return ("".join(chars))
