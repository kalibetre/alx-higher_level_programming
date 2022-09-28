#!/usr/bin/python3
"""Module 5-save_to_json_file

This Module contains a definition for save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """saves the json representation of the object to file"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
