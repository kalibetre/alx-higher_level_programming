#!/usr/bin/python3
"""Module 4-print_square

This Module contains an definition for say_my_name function
"""


def print_square(size):
    """prints a square in #

    Args:
        size (int): the size of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
