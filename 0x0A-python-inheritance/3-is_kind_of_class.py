#!/usr/bin/python3
"""Module 3-is_kind_of_class

This Module contains a definition for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is kind of type a_class

    Args:
        obj: the object
        a_class: expected type

    Returns: True if it is otherwise False
    """
    return isinstance(obj, a_class)
