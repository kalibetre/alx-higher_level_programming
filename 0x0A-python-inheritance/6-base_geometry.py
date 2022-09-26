#!/usr/bin/python3
"""Module 5-base_geometry

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
