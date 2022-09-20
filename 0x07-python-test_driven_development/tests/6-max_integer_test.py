#!/usr/bin/python3
"""Module 6-max_integer_test

This Module contains tests for max_integer function
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""

    def test_module_docstring(self):
        """Tests for module docstring"""
        m_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(m_doc) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        fun_doc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(fun_doc) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        self.assertEqual(max_integer([10]), 10)

    def test_multiple_unordered_elements(self):
        """Tests for unordered numbers list"""
        self.assertEqual(max_integer([10, 3, 43, -1, 0]), 43)
        self.assertEqual(max_integer([43, 3, 43, -1, 0]), 43)
        self.assertEqual(max_integer([-43, -60, -4, -1, 0]), 0)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_ints_and_floats(self):
        """Test for ints and floats"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_floats(self):
        """Test for float only"""
        self.assertEqual(
            max_integer(
                [.00123, .457568, .02345, .23423434, .45675674, .678678,
                    .867090, .74653, .5745375]), 0.86709)

    def test_numeric_string(self):
        """Test for string of numbers"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """Test for string"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """Test list of lists"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Test list of lists of string"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_one_number_in_a_list(self):
        """Test list with single element"""
        self.assertEqual(max_integer([1]), 1)

    def test_mixed_list(self):
        """Test list of lists with different types"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Test mixed int and str types"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Test None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Test dictionary of numbers"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Test a single int number"""
        with self.assertRaises(TypeError):
            max_integer(10)

    def test_float(self):
        """Test a single float number"""
        with self.assertRaises(TypeError):
            max_integer(1.5)
