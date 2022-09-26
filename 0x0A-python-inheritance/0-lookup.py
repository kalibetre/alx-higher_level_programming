#!/usr/bin/python3
"""Module 0-lookup

This Module contains a definition for lookup function
"""


def lookup(obj):
    """gets the list of attributes of an object

    Args:
        obj: the object

    Returns: a list of the obj attributes
    """
    return list(dir(obj))
