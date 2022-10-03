#!/usr/bin/python3
"""Module base

This Module contains a definition for Base Class
"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a Base class

        Args:
            id (int, optional): instance id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list dictionary to a json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the list objects to file"""
        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(
                    [ele.to_dictionary() for ele in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        obj = None
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj
