#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Inherits from list."""

    def is_same_class(obj, a_class):
        """returns True if the object is
        exactly an instance of the specified class.

        Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.
        """
        if type(obj) == a_class:
            return True
        return False
