#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from a_class.


    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.
    """
    if isinstance(obj, a_class):
        return True
    return False
