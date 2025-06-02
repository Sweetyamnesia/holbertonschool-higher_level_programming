#!/usr/bin/python3
"""
This module contains a function that writes an object
to a text file, represented by a JSON string.
"""


import json


def save_to_json_file(my_obj, filename):
    """Function which returns Object to a text file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
