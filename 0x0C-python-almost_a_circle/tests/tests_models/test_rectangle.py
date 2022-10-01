#!/usr/bin/python3
"""Module test_rectangle

This Module contains a tests for Rectangle Class
"""
import unittest

import pycodestyle
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle Class"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/rectangle.py", "tests/tests_models/test_rectangle.py"])
        self.assertEqual(result.total_errors, 0)

    def test_private_vars(self):
        """tests for private variables"""
        with self.assertRaises(AttributeError):
            Rectangle(10, 10).__width
        with self.assertRaises(AttributeError):
            Rectangle(10, 10).__height
        with self.assertRaises(AttributeError):
            Rectangle(10, 10).__x
        with self.assertRaises(AttributeError):
            Rectangle(10, 10).__y

    def test_invalid_args(self):
        """tests for invalid arguments"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_default_initialization_of_properties(self):
        """tests initialization of properties"""
        r1 = Rectangle(10, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_custom_initialization_of_properties(self):
        """tests initialization of properties"""
        r1 = Rectangle(10, 20, 30, 40)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)
