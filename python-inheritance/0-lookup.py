#!/usr/bin/python3
"""
Function that returns the list of available attributes
and methods of an object

Return : a list of object
"""


def lookup(obj):
    return (dir(obj))
