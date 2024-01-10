#!/usr/bin/python3
"""add all arguments to a Python list"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])
# save the updated data
save_to_json_file(data, "add_item.json")
