#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    A class with no class or object attribute
    prevents the user from dynamically creating 
    new instance attributes
    """

    __slots__ = ["first_name"]
