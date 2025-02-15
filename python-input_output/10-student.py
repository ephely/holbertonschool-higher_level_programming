#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Represent a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student."""
        if attrs is None:
            return (self.__dict__)
        result = ({})
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return (result)
