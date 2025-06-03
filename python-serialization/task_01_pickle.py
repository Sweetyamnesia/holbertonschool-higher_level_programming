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

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
         Serializes the current object to a binary file using pickle.
        """
        if not filename:
            return None
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a binary file using pickle.
        """
        if not filename:
            return None
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if not isinstance(obj, cls):
                return None
        except Exception:
            return None
        return obj
