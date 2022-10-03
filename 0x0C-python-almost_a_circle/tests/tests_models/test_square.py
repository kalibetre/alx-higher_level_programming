#!/usr/bin/python3
"""Module test_square

This Module contains a tests for Square Class
"""
import inspect
import io
import sys
import unittest

import pycodestyle
from models import square

Square = square.Square


class TestSquareDocsAndStyle(unittest.TestCase):
    """Tests Base class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/square.py", "tests/tests_models/test_square.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(Square, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(Square.__name__, "Square")


class TestSquare(unittest.TestCase):
    """Test cases for Square Class"""

    def test_private_vars(self):
        """tests for private variables"""
        with self.assertRaises(AttributeError):
            Square(10, 10).__width
        with self.assertRaises(AttributeError):
            Square(10, 10).__height
        with self.assertRaises(AttributeError):
            Square(10, 10).__x
        with self.assertRaises(AttributeError):
            Square(10, 10).__y

    def test_invalid_args(self):
        """tests for invalid arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_default_initialization_of_properties(self):
        """tests initialization of properties"""
        s1 = Square(10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_custom_initialization_of_properties(self):
        """tests initialization of properties"""
        s1 = Square(10, 30, 40)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 30)
        self.assertEqual(s1.y, 40)

    def test_non_int_width_raise_error(self):
        """tests wether type error is raised for non int width property"""
        with self.assertRaises(TypeError) as e:
            Square(10.2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_non_int_x_raise_error(self):
        """tests wether type error is raised for non int x property"""
        with self.assertRaises(TypeError) as e:
            Square(10, {})
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_non_int_y_raise_error(self):
        """tests wether type error is raised for non int y property"""
        with self.assertRaises(TypeError) as e:
            Square(10, 2, 2.3)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_width_and_height_must_be_non_zero_positive(self):
        """tests wether value error exception is raised for negative
        size values
        """
        with self.assertRaises(ValueError) as e:
            Square(-10)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_coordinates_must_be_positive(self):
        """tests wether value error exception is raised for negative
        coordinates
        """
        with self.assertRaises(ValueError) as e:
            Square(10, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            Square(10, 2, -3)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area_of_rect(self):
        """tests that area function returns the correct value"""
        s = Square(10, 10)
        self.assertEqual(s.area(), 100)

    def test_display_one_by_one_rect(self):
        """test if display method works for a one by one square"""
        s = Square(1)
        output_str = io.StringIO()
        sys.stdout = output_str
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), "#\n")

    def test_display_two_by_two_rect(self):
        """test if display method works for a two by three square"""
        r = Square(2)
        output_str = io.StringIO()
        sys.stdout = output_str
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), "##\n##\n")

    def test_display_rect_with_offset(self):
        """test if a square with an offset is displayed correctly"""
        r = Square(2, 2, 2)
        output_str = io.StringIO()
        sys.stdout = output_str
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), "\n\n  ##\n  ##\n")

    def test_display_rect_with_one_side_offset(self):
        """test if a square with a one side offset is displayed correctly"""
        r = Square(3, 1, 0)
        output_str = io.StringIO()
        sys.stdout = output_str
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), " ###\n ###\n ###\n")

    def test_update_of_rect_via_args(self):
        s1 = Square(10, 10, 10)
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")

        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")

        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")

        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_of_rect_when_args_and_kwargs_exist(self):
        s1 = Square(10)
        s1.update(89, 20, x=10, y=10)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 20")

    def test_update_of_rect_when_only_kwargs_exist(self):
        s1 = Square(10, 10)
        s1.update(id=89, size=20, x=10, y=10)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 20")

    def test_string_representation_of_rect(self):
        self.assertEqual(
            str(Square(4, 1, 2, 3)), "[Square] (3) 1/2 - 4"
        )
        s = Square(4, 5)
        self.assertEqual(
            str(s), f"[Square] ({s.id}) 5/0 - 4"
        )
        s = Square(4, 5, 3)
        self.assertEqual(
            str(s), f"[Square] ({s.id}) 5/3 - 4"
        )

    def test_dictionary_representation(self):
        s = Square(10, 1, 9, 1)
        s_dict = s.to_dictionary()
        s_expected_dict = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        self.assertEqual(s_dict, s_expected_dict)
