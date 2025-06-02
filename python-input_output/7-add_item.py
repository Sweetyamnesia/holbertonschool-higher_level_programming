#!/usr/bin/python3
"""
This module contains a script which adds all arguments to a Python list
and save them to a file.
"""


import json


def load_from_json_file(filename):
    """Function which create an object"""
    with open(filename, "r") as file:
        return json.load(file)


def load_from_json_file(filename):
    """Function which create an object"""
    with open(filename, "r") as file:
        return json.load(file)
