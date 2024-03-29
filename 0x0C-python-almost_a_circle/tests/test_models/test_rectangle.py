#!/usr/bin/python3
"""Unittest of the rectangle class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_default_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 4)

    def test_custom_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_height_type(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_invalid_width_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as context:
            r.width = -10
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_invalid_x_type(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as context:
            r.x = {}
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (7) 1/0 - 5/5")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (8) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (8) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (8) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

        r2 = Rectangle(5, 5)
        r2.update(2, width=3)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 5/5")
