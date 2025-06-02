#!/usr/bin/python3
"""
This module contains a function that creates an object
from a JSON files.
"""


import json


def load_from_json_file(filename):
    """Function which create an object"""
    with open(filename, "r") as file:
        return json.load(file)
