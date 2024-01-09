#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Parameters:
    - filename: The name of the file containing the JSON data.

    Returns:
    - The Python object loaded from the JSON file.
    """
    with open(filename, "r") as files:
        return json.load(files)
