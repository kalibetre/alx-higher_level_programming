#!/usr/bin/python3
"""Module 0-add_integer

This Module contains an definition for add integer function
"""


def add_integer(a, b=98):
    """adds two integers or floats

    Args:
        a (int, float): first number
        b (int, float, optional): second number. Defaults to 98.

    Raises:
        TypeError: if a is neither int nor float
        TypeError: if b is neither int nor float

    Returns:
        int: sum of the two numbers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a) if type(a) is float else a
    b = int(b) if type(b) is float else b

    return a + b
