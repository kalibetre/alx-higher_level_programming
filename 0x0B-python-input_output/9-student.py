#!/usr/bin/python3
"""Module 9-student

This Module contains a definition for Student Class
"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a json dict representation of student instance"""
        return self.__dict__
