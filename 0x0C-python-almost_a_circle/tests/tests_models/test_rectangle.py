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

    def test_non_int_width_raise_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10.2, 10)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_non_int_height_raise_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, True)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_non_int_x_raise_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, {})
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_non_int_y_raise_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 2, 2.3)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_width_and_height_must_be_non_zero_positive(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 10)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, -10)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_coordinates_must_be_positive(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 10, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 10, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area_of_rect(self):
        """tests that area function returns the correct value"""
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)
