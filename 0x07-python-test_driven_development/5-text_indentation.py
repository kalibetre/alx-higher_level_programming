#!/usr/bin/python3
"""Module 5-text_indentation

This Module contains an definition for text_indentation function
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of .?:

    Args:
        text (str): the string

    Raises:
        TypeError: raised if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = text.replace(delim, delim + "\n\n")
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
