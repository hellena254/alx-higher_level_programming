#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square:
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """
        Initializes an instance of the Rectangle class.
        Parameter: size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size

    def area(self):
        """implementation of area"""
        return self.__width * self.__height
