#!/usr/bin/python3
"""a function that returns an object represented by a JSON"""
import json


def from_json_string(my_str):
    """a function that returns an object rep by a JSON
    args:
        - my_str: string to be deserialized
    """
    return json.loads(my_str)
