#!/usr/bin/python3
"""A class rectangle"""


class Rectangle:
    """A class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class
        Args: width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width
        Raise:
        TypeError- if value is not an integer
        ValueError - if wisth is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height
        Raise:
        TypeError - if value is not an integer
        ValueError - if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
