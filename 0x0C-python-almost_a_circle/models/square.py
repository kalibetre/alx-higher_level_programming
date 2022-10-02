#!/usr/bin/python3
"""Module square

This Module contains a definition for Square Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a Square instance

        Args:
            size (int): width
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size property of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size property of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates a square instance"""
        if args is not None and len(args) > 0:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.size = value
                elif i == 2:
                    self.x = value
                elif i == 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """returns a string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
