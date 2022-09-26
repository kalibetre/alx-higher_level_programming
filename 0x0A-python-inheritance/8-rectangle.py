#!/usr/bin/python3
"""Module 8-rectangle

This Module contains a definition for Rectangle Class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass of BaseGeometry"""

    def __init__(self, width, height):
        """initializes Rectangle class

        Args:
            width (int): width of the rect
            height (int): height of the rect
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
