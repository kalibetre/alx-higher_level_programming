#!/usr/bin/python3
"""Module 5-save_to_json_file

This Module contains a definition for save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
