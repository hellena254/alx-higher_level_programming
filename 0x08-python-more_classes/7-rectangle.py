#!/usr/bin/python3
"""A class rectangle"""


class Rectangle:
    """A class representing a rectangle
    Attribute:
        number_of_instances - number of instances created
        print_symbol - prints the symbol #
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class
        Args: width and height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """calculate area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        result = []
        for i in range(self.__height):
            [result.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                result.append("\n")
        return ("".join(result))

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """when an instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
