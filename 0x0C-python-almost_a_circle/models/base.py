#!/usr/bin/python3
"""Module base

This Module contains a definition for Base Class
"""


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a Base class

        Args:
            id (int, optional): instance id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
