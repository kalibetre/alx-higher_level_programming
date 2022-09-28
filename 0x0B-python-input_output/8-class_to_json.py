#!/usr/bin/python3
"""Module 8-class_to_json

This Module contains a definition for class_to_json function
"""


def class_to_json(obj: object):
    return obj.__dict__
