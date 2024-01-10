#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_duplicate_max(self):
        """Test with a list containing duplicate max values."""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([42]), 42)

    def test_mixed_types(self):
        """Test with a list containing mixed types."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])
