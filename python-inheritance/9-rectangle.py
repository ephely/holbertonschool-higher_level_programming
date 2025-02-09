#!/usr/bin/python3
"""Create a Rectangle with an import"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeomtry """

    def __init__(self, width, height):
        """ Initialize"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """ Returns the rectangle area """
        return self.__height * self.__width

    def __str__(self):
        """ Return a string representation of the rectangle. """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
