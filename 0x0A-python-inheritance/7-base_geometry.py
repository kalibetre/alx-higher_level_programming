#!/usr/bin/python3
"""Module 7-base_geometry

This Module contains a definition for BaseGeometry Class
"""


class BaseGeometry:
    """A class that is parent of all geometries"""

    def area(self):
        """calculates the area of the geometry

        Raises:
            Exception: Not implemented error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an int variable

        Args:
            name (str): name of the variable
            value (any): expected value

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
