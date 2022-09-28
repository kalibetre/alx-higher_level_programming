#!/usr/bin/python3
"""Module 12-pascal_triangle

This Module contains a definition for pascal_triangle function
"""


def pascal_triangle(n):
    """returns a pascal triangle of n as a list of list"""

    pascal_tri = []
    for n in range(1, n + 1):
        row = [1] * n
        for i in range(1, n - 1):
            row[i] = pascal_tri[n - 2][i - 1] + pascal_tri[n - 2][i]
        pascal_tri.append(row)

    return pascal_tri
