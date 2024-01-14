#!/usr/bin/python3
"""A class rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    """class rectangle inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize an instance of a class
        Args: width, height, x, y, id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve the width of the rectangle"""
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
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve the height of the rectangle"""
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
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """retrieve value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x
        Raise:
        TypeError - if value is not an integer
        ValueError - if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """retrieve value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y
        Raise:
        TypeError - if value is not an integer
        ValueError - if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle with character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" *  self.width)

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

