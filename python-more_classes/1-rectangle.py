#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Square.

        Args:
            width : width of the rectangle.
            height : height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property setter for width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Handle the width errors."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property setter for height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Handle the height errors."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
