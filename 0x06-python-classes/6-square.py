#!/usr/bin/python3
"""Module 6-square

This Module contains an definition for Square class
"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes a square with size

        Args:
            size (int, optional): the size of the square. Defaults to 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position property of the square

        Returns:
            tuple: pair of two positive numbers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the position property

        Args:
            value (tuple): pair of two positive integers

        Raises:
            TypeError: if value is not tuple or the numbers are negative
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area of the square

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square with a #"""
        if (self.size == 0):
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(*[' ' for _ in range(self.position[0])], sep='', end='')
                print(*["#" for _ in range(self.size)], sep='')
