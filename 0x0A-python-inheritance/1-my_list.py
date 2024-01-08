#!/usr/bin/python3
"""A class MyList that inherits from List"""


class MyList(list):
    """My list prints the list in ascending order"""
    def __init__(self):
        """constructor of the objects"""
        super().__init__()

    def print_sorted(self):
        """print the list"""
        sort_list = sorted(self)
        print(sort_list)
