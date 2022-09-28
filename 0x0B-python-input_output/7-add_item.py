#!/usr/bin/python3
"""Module 7-add_item

This Module contains a script to read and update a json file
"""

from os import path
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """reads a list from file and appends the arguments to it"""
    filename = "add_item.json"
    data = list(load_from_json_file(filename)) if path.exists(filename) else []
    for i in range(1, len(argv)):
        data.append(argv[i])
    save_to_json_file(data, filename)


if __name__ == "__main__":
    main()
