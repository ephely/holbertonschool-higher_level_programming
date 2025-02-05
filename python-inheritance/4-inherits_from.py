#!/usr/bin/python3
"""Defines a class and inherited (directly or indirectly)."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited.


    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
