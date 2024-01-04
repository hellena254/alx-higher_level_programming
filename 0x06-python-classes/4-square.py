#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int, optional): The size of the square. Defaults to 0.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must br an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Getter method for retrieving size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate the area of the square"""
        return (self.__size ** 2)
