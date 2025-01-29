#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size : Size of the square.
            position : Position of a square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """property setter for position."""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        """property setter for position."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
