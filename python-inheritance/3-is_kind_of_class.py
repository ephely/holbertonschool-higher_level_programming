#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from a_class.


    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.
    """
    return isinstance(obj, a_class)
