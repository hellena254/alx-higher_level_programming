#!/usr/bin/python3
"""Unittest of the rectangle class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_default_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_custom_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
