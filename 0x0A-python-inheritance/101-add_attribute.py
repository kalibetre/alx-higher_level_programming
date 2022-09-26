#!/usr/bin/python3
"""Module 101-add_attribute

This Module contains a definition for add_attribute function
"""


def add_attribute(obj: object, name, value):
    """adds new attribute to the given object

    Args:
        obj (object): the object
        name (str): name of the attribute
        value (any): value of the attribute

    Raises:
        TypeError: raised if attribute can't be added to the object
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
