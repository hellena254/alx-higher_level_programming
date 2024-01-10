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
    # Get the dictionary of attributes and their values for the object
    obj_dict = obj.__dict__.copy()

    # Convert non-serializable attributes to serializable types
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict)):
            obj_dict[key] = value
        elif isinstance(value, bool):
            obj_dict[key] = value
        elif isinstance(value, int):
            obj_dict[key] = value
        elif isinstance(value, str):
            obj_dict[key] = value
        else:
            # Handle other types (e.g., custom class instances)
            obj_dict[key] = str(value)

    return obj_dict
