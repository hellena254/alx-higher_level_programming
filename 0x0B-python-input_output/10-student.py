#!/usr/bin/python3
"""A class Student to JSON"""


class Student:
    """A class student"""
    def __init__(self, first_name, last_name, age):
        """
        Initialize an instance
        Args: first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
       if atttrs is None:
             return (self.__dict__)

        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)

        return filtered_dict
