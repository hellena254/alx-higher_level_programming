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
        """set the width of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """retrieve value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x co-ordinate"""
        self.__x = value

    @property
    def y(self):
        """retrieve value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y value"""
        self.__y = value
