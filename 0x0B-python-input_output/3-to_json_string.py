#!/usr/bin/python3
""" function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object
    args:
        - my_obj: object to be serialized
    """
    return json.dumps(my_obj)
