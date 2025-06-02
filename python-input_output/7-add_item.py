#!/usr/bin/python3
"""
This module contains a script which adds all arguments to a Python list
and save them to a file.
"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
with open(filename, 'a', encoding="utf-8") as file:
    my_list = []
    my_list.append(args[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
