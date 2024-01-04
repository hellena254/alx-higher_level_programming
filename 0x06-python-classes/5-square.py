#!/usr/bin/python3
class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
        value (int): The new size of the square.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """print the square using the cjaracter # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
