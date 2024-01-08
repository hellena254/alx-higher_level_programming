#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes an instance of the Rectangle class.
        Parameters:
        - width: Width of the rectangle (positive integer).
        - height: Height of the rectangle (positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
