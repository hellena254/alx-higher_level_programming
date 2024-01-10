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
        if (type(attrs) == list and all(type(attr) == str for attr in attrs)):
            return {t: getattr(self, t) for t in attrs if hasattr(self, t)}
        return (self.__dict__)

    def reload_from_json(self, json):
    """
    replaces all attributes of the Student instance
    args:
        json - the dict to replace attributes with
    """
        for a, b in json.items():
            setattr(self, a, b)
    
