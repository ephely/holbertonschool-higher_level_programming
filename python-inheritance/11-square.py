#!/usr/bin/python3
"""Create a Square with an import"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""

    def __init__(self, size):
        """ Initialize """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """ Return a string representation of Square """
        return ("[Square] {}/{}".format(self.__size, self.__size))
