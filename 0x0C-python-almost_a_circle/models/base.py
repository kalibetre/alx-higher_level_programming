#!/usr/bin/python3
"""Module base

This Module contains a definition for Base Class
"""
import csv
import json
import turtle
from random import randint


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
            wr = csv.writer(f)
            if list_objs is None:
                f.write("")
            else:
                for ele in list_objs:
                    if cls.__name__ == "Rectangle":
                        wr.writerow(
                            [ele.id, ele.width, ele.height, ele.x, ele.y]
                        )
                    else:
                        wr.writerow([ele.id, ele.size, ele.x, ele.y])

    @classmethod
    def load_from_file_csv(cls):
        """loads objects from a csv file"""
        try:
            with open(f"{cls.__name__}.csv", "r") as f:
                r = csv.reader(f)
                elms = []
                for row in r:
                    obj_dict = {"id": row[0], }
                    if cls.__name__ == "Rectangle":
                        obj_dict["width"] = int(row[1])
                        obj_dict["height"] = int(row[2])
                        obj_dict["x"] = int(row[3])
                        obj_dict["y"] = int(row[4])
                    else:
                        obj_dict["size"] = int(row[1])
                        obj_dict["x"] = int(row[2])
                        obj_dict["y"] = int(row[3])
                    elms.append(cls.create(**obj_dict))
                return elms
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws a list of rectangles and squares using turtle library"""
        wn = turtle.Screen()
        wn.bgcolor("white")
        wn.title("ALX Python Full Circle")

        colors = [
            "gold", "orange", "red", "maroon", "violet",
            "magenta", "purple", "navy", "blue", "skyblue", "cyan",
            "turquoise", "lightgreen", "green", "darkgreen",
            "chocolate", "brown", "black", "gray"
        ]
        for rect in list_rectangles:
            pencolor = colors[randint(0, len(colors) - 1)]
            fillcolor = pencolor
            Base.draw_obj("Rectangle", rect, pencolor, fillcolor)
        for square in list_squares:
            pencolor = colors[randint(0, len(colors) - 1)]
            fillcolor = pencolor
            Base.draw_obj("Square", square, pencolor, fillcolor)

        turtle.done()

    @staticmethod
    def draw_obj(type, obj, pencolor, fillcolor):
        """Draws a single object using turtle library"""
        props = obj.to_dictionary()
        x = props["x"]
        y = props["y"]
        width = None
        height = None
        if type == "Rectangle":
            width = props["width"]
            height = props["height"]
        else:
            width = props["size"]
            height = width

        turtle.penup()
        turtle.begin_fill()
        turtle.color(pencolor)
        turtle.fillcolor(fillcolor)
        turtle.setpos(x, y)
        turtle.pendown()
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.end_fill()
