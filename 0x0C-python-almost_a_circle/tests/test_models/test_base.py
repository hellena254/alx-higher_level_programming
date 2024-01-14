#!/usr/bin/python3
"""Unittest for base.py"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_default_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_mixed_ids(self):
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_multiple_instances(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 5)
