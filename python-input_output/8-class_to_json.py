#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description with simple data structure for JSON serialization of an object.
"""


import json


def class_to_json(obj):
	"""
	Function that returns dictionary description of an object
	"""
	return obj.__dict__
	
