#!/usr/bin/python3
"""a function that appends a string"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file
    args:
        - filename: name of the file
        - text: text to append to the file
    Returns:
        - number of characters added
    """
    with open(filename, "a", encoding="utf-8") as files:
        return (files.write(text))
