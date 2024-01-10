#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Initialize an empty line
    current_line = ""
     # Iterate through each character in the text
    for char in text:
        # If the character is ., ?, or :, print the current line and reset it
        if char in ".?:":
            print(current_line.strip())
            print("")
            current_line = ""
        else:
            current_line += char

    # Print the last line (if any)
    if current_line:
        print(current_line.strip())
