#!/usr/bin/python3
"""
This module defines the add_integer function.
The add_integer function adds two integers or floats
and returns the result as an integer.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum as an integer.
    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default: 98).
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
