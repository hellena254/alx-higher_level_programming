#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Check if the given object is exactly an instance of the specified class.
    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare with.

    Returns:
    - True if obj is exactly an instance of a_class;
    otherwise, False.
    """
    if type(obj) == a_class:
        return True
    return False
