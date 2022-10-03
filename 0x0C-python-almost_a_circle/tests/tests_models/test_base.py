#!/usr/bin/python3
"""Module test_base

This Module contains a tests for Base Class
"""
import unittest

import pycodestyle
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test cases for Base Class"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/base.py", "tests/tests_models/test_base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_initial_id_set_to_one(self):
        """Tests if initial value of id is set to 1"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_custom_id(self):
        """tests assignment of custom id"""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_successive_init_increases_id(self):
        """Tests successive calls to init increments id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id - b1.id, 1)

    def test_private_var(self):
        """tests for private variables"""
        with self.assertRaises(AttributeError):
            Base().__nb_objects

    def test_invalid_args(self):
        """tests for invalid arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_with_none_and_empty_list(self):
        """tests to json string with None and empty list"""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, '[]')
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, '[]')

    def test_to_json_string(self):
        """tests to json string with valid data"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        json_str = Base.to_json_string([r1_dict])
        self.assertEqual(
            json_str, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        )

    def test_save_to_file(self):
        """test whether the static method save_to_file saves the correct
        json representation to file
        """
        r1 = Rectangle(10, 7, 3, 2, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)

        Rectangle.save_to_file([r1, r2])

        expected_str = (
            '[{"id": 1, "width": 10, "height": 7, "x": 3, "y": 2}, '
            '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), expected_str)

    def test_save_to_file_empty(self):
        """test whether the static method save_to_file saves the correct
        json representation to file for None value
        """
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_string(self):
        """tests the conversion of string to list object"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_from_empty_json_string(self):
        """tests the conversion of string to list object"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])
