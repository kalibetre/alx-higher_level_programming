#!/usr/bin/python3
"""Module 4-inherits_from

This Module contains a definition for inherits_from function
"""


def inherits_from(obj, a_class):
    """
    checks if obj is subclass of type a_class

    Args:
        obj: the object
        a_class: expected type

    Returns: True if it is otherwise False
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
