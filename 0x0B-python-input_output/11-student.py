#!/usr/bin/python3
"""Module 11-student

This Module contains a definition for Student Class
"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json dict representation of student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return dict(filter(lambda x: x[0] in attrs, self.__dict__.items()))

    def reload_from_json(self, json):
        for item in json.items():
            self.__dict__[item[0]] = item[1]
