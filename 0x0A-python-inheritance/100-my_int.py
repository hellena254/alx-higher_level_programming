#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """class MyInt inherits from int"""
    def __eq__(self, other):
        """Inverted equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted inequality operator"""
        return super().__eq__(other)
