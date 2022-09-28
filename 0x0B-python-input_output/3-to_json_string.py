#!/usr/bin/python3
"""Module 3-to_json_string 

This Module contains a definition for to_json_string function
"""
import json


def to_json_string(my_obj):
    """returns the json string representation of the object"""
    return json.dumps(my_obj)
