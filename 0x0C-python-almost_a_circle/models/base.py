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
        """loads object from json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an object from a dictionary of attributes"""
        obj = None
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """loads objects from a json file"""
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                elms = []
                objs = cls.from_json_string(f.read())
                for obj in objs:
                    elms.append(cls.create(**obj))
                return elms
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves the list objects to a csv file"""
        with open(f"{cls.__name__}.csv", "w") as f:
            if list_objs is None:
                f.write("")
            else:
                for ele in list_objs:
                    ele_dict = dict(ele.to_dictionary())
                    id = ele_dict["id"]
                    x = ele_dict["x"]
                    y = ele_dict["y"]
                    if cls.__name__ == "Rectangle":
                        width = ele_dict["width"]
                        height = ele_dict["height"]
                        f.write(f"{id},{width},{height},{x},{y}\n")
                    else:
                        size = ele_dict["size"]
                        f.write(f"{id},{size},{x},{y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """loads objects from a csv file"""
        try:
            with open(f"{cls.__name__}.csv", "r") as f:
                elms = []
                lines = f.readlines()
                for line in lines:
                    props = line.split(",")
                    obj_dict = {"id": props[0]}
                    if cls.__name__ == "Rectangle":
                        obj_dict["width"] = int(props[1])
                        obj_dict["height"] = int(props[2])
                        obj_dict["x"] = int(props[3])
                        obj_dict["y"] = int(props[4])
                    else:
                        obj_dict["size"] = int(props[1])
                        obj_dict["x"] = int(props[2])
                        obj_dict["y"] = int(props[3])
                    elms.append(cls.create(**obj_dict))
                return elms
        except FileNotFoundError:
            return []
