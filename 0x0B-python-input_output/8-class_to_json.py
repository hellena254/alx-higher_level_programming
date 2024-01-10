#!/usr/bin/python3
"""Class To JSON"""


def class_to_json(obj):
    """
    Convert an instance of a class to a dictionary for JSON serialization.

    Parameters:
    - obj: An instance of a class.

    Returns:
    - A dictionary representing the serialized object.
    """
    return (obj.__dict__)
