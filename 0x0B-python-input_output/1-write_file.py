#!/usr/bin/python3
"""Write a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file.
    Args:
       filename (str): The name of the file to write.
       text (str): The text to write to the file.
    Returns:
       The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as files:
        return (files.write(text))
