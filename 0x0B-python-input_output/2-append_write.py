#!/usr/bin/python3
"""Module 2-append_file

This Module contains a definition for append_file function
"""


def append_write(filename="", text=""):
    """appends a text to file encoded with utf-8"""
    bytes_wrt = 0
    with open(filename, "a", encoding="utf-8") as f:
        bytes_wrt = f.write(text)
    return bytes_wrt
