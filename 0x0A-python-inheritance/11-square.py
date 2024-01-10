#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """
        Initializes an instance of the Rectangle class.
        Parameter: size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size
