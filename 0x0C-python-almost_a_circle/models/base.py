#!/usr/bin/python3
"""The Base Class"""


class Base:
    """The base class
    private class attribute:
        __nb_object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of a class
        args: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
