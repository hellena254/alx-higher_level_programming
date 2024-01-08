!/usr/bin/python3
"""check if the object is an instance of a class that inherited from the specified class """


def inherits_from(obj, a_class):
    """
    Check if the given object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare with.
    Returns:
    - True if obj is an instance of a class inherited from a_class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

