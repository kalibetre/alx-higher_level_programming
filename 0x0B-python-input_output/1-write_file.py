#!/usr/bin/python3
"""Module 1-write_file

This Module contains a definition for write_file function
"""


def write_file(filename="", text=""):
    """writes a text to file encoded with utf-8"""
    bytes_wrt = 0
    with open(filename, "w", encoding="utf-8") as f:
        bytes_wrt = f.write(text)
    return bytes_wrt
