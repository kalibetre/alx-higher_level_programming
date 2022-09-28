#!/usr/bin/python3
"""Module 4-from_json_string

This Module contains a definition for from_json_string function
"""
import json


def from_json_string(my_obj):
    """returns the object form json string representation"""
    return json.loads(my_obj)
