#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, mode="", encoding="utf-8") as files:
        return(files.write(text))
