#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width : width of the rectangle.
            height : height of the rectangle.
        """
        self.width = width
        self.height = height

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

    def area(self):
        """Returns the current rectangle area."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the current rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the rectangle with the character #."""
        if self.width == 0 or self.height == 0:
            return ""

        rect_lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
