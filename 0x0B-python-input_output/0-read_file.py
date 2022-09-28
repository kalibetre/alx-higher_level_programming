#!/usr/bin/python3
"""Module 0-read_file

This Module contains a definition for read_file function
"""


def read_file(filename=""):
    """reads a text file encoded with utf-8"""
    with open(filename, "r", encoding="utf-8") as f:
        print(*(f.readlines()), sep="")
