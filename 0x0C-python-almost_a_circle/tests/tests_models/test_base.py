#!/usr/bin/python3
"""Module test_base

This Module contains a tests for Base Class
"""
import inspect
import os
import unittest

import pycodestyle
from models import base
from models.rectangle import Rectangle
from models.square import Square

Base = base.Base


class TestBaseDocsAndStyle(unittest.TestCase):
    """Tests Base class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/base.py", "tests/tests_models/test_base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(Base, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(Base.__name__, "Base")


class TestBase(unittest.TestCase):
    """Test cases for Base Class"""

    def tearDown(self) -> None:
        """removes temporary files used for testing"""
        temp_files = ["Rectangle.json", "Rectangle.csv",
                      "Square.json", "Square.csv"]
        for file in temp_files:
            try:
                os.remove(file)
            except OSError:
                pass

    def test_invalid_args(self):
        """tests for invalid arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_private_var(self):
        """tests for private variables"""
        with self.assertRaises(AttributeError):
            Base().__nb_objects

        with self.assertRaises(AttributeError):
            Base().nb_objects

    def test_initial_id_set_to_one(self):
        """Tests if initial value of id is set to 1"""
        self.assertTrue(Base(), self.id == 1)

    def test_custom_id(self):
        """tests assignment of custom id"""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_successive_init_increases_id(self):
        """Tests successive calls to init increments id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id - b1.id, 1)

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

    def test_create_class_method(self):
        """test if objects are returned from a dictionary"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

        s1 = Square(3, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_load_from_file_raises_exception(self):
        """tests for non existent file"""
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """tests the load from file class method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(r1.to_dictionary(),
                         list_rectangles_input[0].to_dictionary())
        self.assertEqual(r2.to_dictionary(),
                         list_rectangles_input[1].to_dictionary())

    def test_csv_file_io_rect(self):
        """tests csv file io for rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(r1.to_dictionary(),
                         list_rectangles_input[0].to_dictionary())
        self.assertEqual(r2.to_dictionary(),
                         list_rectangles_input[1].to_dictionary())

    def test_csv_file_io_sq(self):
        """test csv file io for Square"""
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        list_rectangles_input = [s1, s2]

        Square.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Square.load_from_file_csv()

        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(s1.to_dictionary(),
                         list_rectangles_input[0].to_dictionary())
        self.assertEqual(s2.to_dictionary(),
                         list_rectangles_input[1].to_dictionary())

    def test_csv_file_from_non_existing(self):
        """test csv file loading from non existent file"""
        try:
            os.remove("Square.json")
        except Exception:
            pass
        self.assertEqual(Square.load_from_file_csv(), [])
