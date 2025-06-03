#!/usr/bin/python3
"""
This module contains a script which adds all arguments to a Python list
and save them to a file.
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """Function which returns Object to a text file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Function which create an object"""
    with open(filename, "r") as file:
        return json.load(file)


args = sys.argv[1:]
filename = "add_item.json"
with open(filename, 'w', encoding="utf-8") as file:
    my_list = load_from_json_file(filename)
    save_to_json_file(my_list, filename)
