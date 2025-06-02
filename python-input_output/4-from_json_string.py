#!/usr/bin/python3
"""
This module contains a function that returns an object
represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """Function which returns python data structures"""
    res = json.loads(my_str)
    return res
