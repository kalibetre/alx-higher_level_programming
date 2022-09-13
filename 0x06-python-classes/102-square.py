#!/usr/bin/python3
"""Module 102-square

This Module contains an definition for Square class
"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """initializes a square with size

        Args:
            size (int, optional): the size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """the size property of the square

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """the setter of the private property __size

        Args:
            value (int): the value to be used

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def __eq__(self, __o):
        return __o and self.size == __o.size

    def __ne__(self, __o):
        return not self.__eq__(__o)

    def __lt__(self, __o):
        return self.size < __o.size

    def __le__(self, __o):
        return self.size <= __o.size

    def __gt__(self, __o):
        return self.size > __o.size

    def __ge__(self, __o):
        return self.size >= __o.size
