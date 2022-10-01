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
        self.__y = value
