#!/usr/bin/python3
"""Module 103-magic_class

This Module contains an definition for Square class
"""


import math


class MagicClass:
    """Magic class"""

    def __init__(self, radius=0):
        """Initializes a magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returns the area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference of a circle"""
        return 2 * math.pi * self.__radius
