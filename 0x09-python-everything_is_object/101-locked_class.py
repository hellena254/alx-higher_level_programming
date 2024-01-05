#!/usr/bin/python3
class LockedClass:
    """A class with no class or object attribute
    prevents the user from dynamically creating 
    new instance attributes
    """
    __slots__ = ['first_name']
