#!/usr/bin/env python3

"""
This module is used to learn how to serialize and deserialize
custom Python objects using the pickle module.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
         Serializes the current object to a binary file using pickle.
        """
        with open(filename, "wb") as file:
            pickle.dump(filename, file)
        pass


@classmethod
def deserialize(cls, filename):
    """
    Deserializes an object from a binary file using pickle.
    """
    with open(filename, "rb") as file:
        return pickle.load(file)
    pass
