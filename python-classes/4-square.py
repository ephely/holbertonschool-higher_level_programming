#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size : Size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """property setter for size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Handle the errors."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)
