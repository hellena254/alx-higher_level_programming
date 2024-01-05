#!/usr/bin/python3
def magic_string():
    magic_string.a = getattr(magic_string, 'a', 0) + 1
    return ", ".join(["BestSchool"] * magic_string.a)
