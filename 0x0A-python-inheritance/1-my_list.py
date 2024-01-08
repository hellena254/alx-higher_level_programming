#!/usr/bin/python3
"""A class MyList that inherits from List"""


def list(obj):
    dir(obj)

class MyList(list):
    """My list prints the list in ascending order"""
    def print_sorted(self):
       sort_list = sorted(self)
       print(sort_list)
