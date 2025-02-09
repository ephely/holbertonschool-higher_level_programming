#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal.
    """
    pass

    @abstractmethod
    def sound(self):
        """ Defines the sound for animals. """
        pass


class Dog(Animal):
    """
    A class representing a dog, inheriting from Animal.
    """
    def sound(self):
        """ Defines the sound for a dog. """
        return ("Bark")


class Cat(Animal):
    """
    A class representing a cat, inheriting from Animal.
    """
    def sound(self):
        """ Defines the sound for a cat. """
        return ("Meow")
