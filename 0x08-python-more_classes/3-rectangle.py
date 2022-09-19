#!/usr/bin/python3
"""Module 3-rectangle

This Module contains an definition for Rectangle class
"""


class Rectangle:
    """A class to represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle with width and height

        Args:
            width (int, optional): width of the rect. Defaults to 0.
            height (int, optional): height of the rect. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width property setter

        Args:
            value (int): value

        Raises:
            TypeError: if width is not an int
            ValueError: if width is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height property setter

        Args:
            value (int): value

        Raises:
            TypeError: if height is not an int
            ValueError: if height is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle

        Returns:
            int: area
        """
        return self.height * self.width

    def perimeter(self):
        """calculates the perimeter of the rectangle

        Returns:
            int: perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """returns a string representation of the rectangle"""
        rec_str = ""
        if (self.width == 0 or self.height == 0):
            return rec_str

        rows = ["#" * self.width for _ in range(self.height)]
        rec_str = "\n".join(rows)
        return rec_str
