#!/usr/bin/python3
"""check if the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare with.
    Returns:
    - True if obj is an instance of or inherited from a_class; otherwise, False.
    """
    return isinstance(obj, a_class)
