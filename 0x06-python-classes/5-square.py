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
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >- 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
        int: The size of the square.
        """
        return (self.__size)

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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the current square area.

        Returns:
        int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints to the stdout the square with character #
        If size = 0, prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
