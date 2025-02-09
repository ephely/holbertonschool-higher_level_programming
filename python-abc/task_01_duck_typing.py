#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    An abstract base class representing Shapes.
    """
    pass

    @abstractmethod
    def area(self):
        """ Defines the area of shapes. """
        pass

    @abstractmethod
    def perimeter(self):
        """ Defines the perimeter of shapes. """
        pass


def shape_info(shape):
    """ Print the area and perimeter of shapes. """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


class Circle(Shape):
    """
    A class representing a circle.
    """

    def __init__(self, radius):
        """ Initialize a Circle. """
        self.radius = abs(radius)

    def area(self):
        """ Calculate and return the area of a circle. """
        return (math.pi * self.radius ** 2)

    def perimeter(self):
        """ Calculate and return the perimeter of a circle. """
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """ A class representing a rectangle. """

    def __init__(self, width, height):
        """ Initialize a Rectangle. """
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of the rectangle. """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Return the perimeter of the rectangle. """
        return (self.__height + self.__width) * 2
