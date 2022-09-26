#!/usr/bin/python3
"""Module 2-is_same_class

This Module contains a definition for is_same_class function
"""


def is_same_class(obj, a_class):
    """
    checks if obj is exactly of type a_class

    Args:
        obj: the object
        a_class: expected type

    Returns: True if it is otherwise False
    """
    return type(obj) is a_class
