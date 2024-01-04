#!/usr/bin/python3
import math

class MagicClass:
    """
    A class representing a magical circle.

    Attributes:
    __radius (float): The radius of the magical circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Args:
        radius (int or float, optional): The radius of the magical circle. Defaults to 0.
        Raises:
        TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the magical circle.

        Returns:
        float: The area of the magical circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Computes and returns the circumference of the magical circle.

        Returns:
        float: The circumference of the magical circle.
        """
        return (2 * math.pi * self.__radius)
