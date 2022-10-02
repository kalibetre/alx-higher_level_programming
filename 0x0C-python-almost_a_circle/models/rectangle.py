#!/usr/bin/python3
"""Module base

This Module contains a definition for Base Class
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a Rectangle instance

        Args:
            width (int): width
            height (int): width
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property for width of the rectangle

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width property

        Args:
            value (int): width
        """
        self.validate_int("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property for the rectangle

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height property

        Args:
            value (int): height
        """
        self.validate_int("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property for x coordinate

        Returns:
            int: x coord
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x coord property

        Args:
            value (int): x coord
        """
        self.validate_int("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property for y coord of the rectangle

        Returns:
            int: y coord
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y coord of the rectangle

        Args:
            value (int): y coord
        """
        self.validate_int("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def validate_int(self, name, value):
        """validates an int variable

        Args:
            name (str): name of the variable
            value (any): value to be checked

        Raises:
            TypeError: raised if value is not an int
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

    def area(self):
        """calculates the area of the rectangle

        Returns:
            int: area of rect
        """
        return self.width * self.height
