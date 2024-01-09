#!/usr/bin/python3
"""a function that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file
    args:
        my_obj - the object to be written
        filename - the filename
    """
    with open(filename, "w") as files:
        # use json.dump to write the object to the file in JSON
        json.dump(my_obj, files)
