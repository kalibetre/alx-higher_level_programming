#!/usr/bin/python3
"""Module 6-load_from_json_file

This Module contains a definition for load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """reads the json representation of the object from file"""
    obj_json = None
    with open(filename, "r") as f:
        obj_json = f.read()
    return json.loads(obj_json)
