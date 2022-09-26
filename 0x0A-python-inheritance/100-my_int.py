#!/usr/bin/python3
"""Module 100-my_int

This Module contains a definition for MyInt Class
"""


class MyInt(int):
    """MyInt subclass of int"""

    def __eq__(self, __x):
        """overrides equals magic method"""
        return not super().__eq__(__x)

    def __ne__(self, __x):
        """overrides not equals magic method"""
        return not super().__ne__(__x)
