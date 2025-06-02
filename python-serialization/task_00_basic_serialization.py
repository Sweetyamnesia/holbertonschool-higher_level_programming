#!/usr/bin/env python3

"""
This module adds the functionality to serialize a Python dictionary
to a JSON file and deserialize the JSON file to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Function with Python Dictionary with data and
    the filename of the ouput JSON file
    """
    with open(filename, "w") as file:
        json.dump(data, file)
    pass


def load_and_deserialize(filename):
    """
    Function with the filename of the input JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
    pass
