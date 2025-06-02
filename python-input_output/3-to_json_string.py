#!/usr/bin/python3
"""
This module contains a function that returns JSON
representation of an object (string).
"""


import json

def to_json_string(my_obj):
    """Function which returns the JSON string"""
    res = json.dumps(my_obj)
    return res
