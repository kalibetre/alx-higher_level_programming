#!/usr/bin/python3
"""Module 100-append_after

This Module contains a definition for append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends the given string after the line containing the search string"""
    lines = []
    with open(filename, "r+") as f:
        for line in f.readlines():
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        f.seek(0)
        f.writelines(lines)
