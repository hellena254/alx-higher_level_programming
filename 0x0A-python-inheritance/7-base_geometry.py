#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """a base class for geomtery classes"""
    def __init__(self):
        """Initializes an instance of the BaseGeometry class"""
        pass

    def area(self):
        """ Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates the given value as an integer.
        Parameters: name and value
        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
