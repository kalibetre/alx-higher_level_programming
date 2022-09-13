#!/usr/bin/python3
"""Module 2-square

This Module contains an definition for Square class
"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """initializes a square with size

        Args:
            size (int, optional): the size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
