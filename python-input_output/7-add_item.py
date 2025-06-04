#!/usr/bin/python3
"""
This module contains a script which adds all arguments to a Python list
and save them to a file.
"""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""
Try to load existing list from file
"""
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

"""
Add new arguments (excluding the script name)
"""
items.extend(sys.argv[1:])

"""
Save updated list to file
"""
save_to_json_file(items, filename)
