#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file, after each line containing a specific string
    Parameters:
    - filename (str): The name of the file to modify.
    - search_string (str): The string to search for in each line.
    - new_string (str): The line of text to insert after each line containing the search string.
    """
    with open(filename, "r") as files:
        lines = files.readlines()

    with open(filename, "w") as files:
        for line in lines:
            files.write(line)
            if search_string in line:
                files.write(new_string)
