#!/usr/bin/python3
# 2-square.py
"""defines a class Square"""


class Square:
    """Attributes: __size (int): size of the square"""

    def __init__(self, size=0):
        """Initializes a new instance of the square class.
            Args: size (int): size of the square
            Raises:
            TypeError: If size is not an integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
