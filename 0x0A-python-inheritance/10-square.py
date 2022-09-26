#!/usr/bin/python3
"""Module 10-square

This Module contains a definition for Square Class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle"""

    def __init__(self, size):
        """initializes Square class

        Args:
            width (int): width of the rect
            height (int): height of the rect
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
