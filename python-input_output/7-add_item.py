#!/usr/bin/python3
"""
This module contains a script which adds all arguments to a Python list
and save them to a file.
"""


import sys
import json


args = sys.argv[1:]
filename = "add_item.json"
with open(filename, 'w', encoding="utf-8") as file:
    json.dump(args, file)
