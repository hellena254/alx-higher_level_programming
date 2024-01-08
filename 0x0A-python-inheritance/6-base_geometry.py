#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """a base class for geomtery classes"""
    def __init__(self):
        """Initializes an instance of the BaseGeometry class"""
        pass

    def area(self):
        """ Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")
