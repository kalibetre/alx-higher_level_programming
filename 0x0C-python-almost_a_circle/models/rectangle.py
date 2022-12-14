#!/usr/bin/python3
"""Module rectangle

This Module contains a definition for Rectangle Class
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

    def display(self):
        """prints the rectangle instance with #"""
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(*[' ' for _ in range(self.x)], sep='', end='')
            print(*["#" for _ in range(self.width)], sep='')

    def update(self, *args, **kwargs):
        """updates a rectangle instance"""
        if args is not None and len(args) > 0:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.width = value
                elif i == 2:
                    self.height = value
                elif i == 3:
                    self.x = value
                elif i == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """returns a string representation of the rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def to_dictionary(self):
        """returns a dictionary representation"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
