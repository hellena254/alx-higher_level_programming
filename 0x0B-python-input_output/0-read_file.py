#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as files:
        print(files.read(), end="")
