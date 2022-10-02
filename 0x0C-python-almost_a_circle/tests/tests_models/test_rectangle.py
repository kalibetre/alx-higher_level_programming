#!/usr/bin/python3
"""Module test_rectangle

This Module contains a tests for Rectangle Class
"""
import io
import sys
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
        """tests wether type error is raised for non int width property"""
        with self.assertRaises(TypeError) as e:
            Rectangle(10.2, 10)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_non_int_height_raise_error(self):
        """tests wether type error is raised for non int height property"""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, True)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_non_int_x_raise_error(self):
        """tests wether type error is raised for non int x property"""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, {})
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_non_int_y_raise_error(self):
        """tests wether type error is raised for non int y property"""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 2, 2.3)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_width_and_height_must_be_non_zero_positive(self):
        """tests wether value error exception is raised for negative
        width and height values
        """
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 10)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, -10)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_coordinates_must_be_positive(self):
        """tests wether value error exception is raised for negative
        coordinates
        """
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

    def test_display_one_by_one_rect(self):
        """test if display method works for a one by one rect"""
        r = Rectangle(1, 1)
        output_str = io.StringIO()
        sys.stdout = output_str
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), "#\n")

    def test_display_two_by_three_rect(self):
        """test if display method works for a two by three rect"""
        r = Rectangle(2, 3)
        output_str = io.StringIO()
        sys.stdout = output_str
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), "##\n##\n##\n")

    def test_display_rect_with_offset(self):
        """test if a rectangle with an offset is displayed correctly"""
        r = Rectangle(2, 3, 2, 2)
        output_str = io.StringIO()
        sys.stdout = output_str
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_rect_with_one_side_offset(self):
        """test if a rectangle with a one side offset is displayed correctly"""
        r = Rectangle(3, 2, 1, 0)
        output_str = io.StringIO()
        sys.stdout = output_str
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output_str.getvalue(), " ###\n ###\n")

    def test_update_of_rect_via_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_of_rect_when_args_and_kwargs_exist(self):
        r1 = Rectangle(10, 10)
        r1.update(89, 20, x=10, y=10)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 20/10")

    def test_update_of_rect_when_only_kwargs_exist(self):
        r1 = Rectangle(10, 10)
        r1.update(id=89, width=20, height=20, x=10, y=10)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 20/20")

    def test_string_representation_of_rect(self):
        self.assertEqual(
            str(Rectangle(4, 5, 1, 2, 3)), "[Rectangle] (3) 1/2 - 4/5"
        )
        r = Rectangle(4, 5)
        self.assertEqual(
            str(r), f"[Rectangle] ({r.id}) 0/0 - 4/5"
        )
        r = Rectangle(4, 5, 3)
        self.assertEqual(
            str(r), f"[Rectangle] ({r.id}) 3/0 - 4/5"
        )

    def test_dictionary_representation(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        r1_expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dict, r1_expected_dict)
