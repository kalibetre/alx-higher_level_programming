#!/usr/bin/python3
"""Module 3-say_my_name

This Module contains an definition for say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """prints a formatted string with the given variables

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: first_name must be str
        TypeError: last_name must be str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
