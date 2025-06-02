#!/usr/bin/env python3
from abc import ABC, abstractmethod   # For creating abstract base classes
from math import pi   # Provides access to mathematical functions and constants


class Shape(ABC):
    @abstractmethod
    def area(self):
        # Method to compute the area
        pass

    @abstractmethod
    def perimeter(self):
        # Method to compute the perimeter
        pass


class Circle(Shape):
    def __init__(self, radius):
        # Initialize circle with a given radius
        self.radius = radius

    def area(self):
        # Compute and return the area of the circle
        return pi * self.radius ** 2

    def perimeter(self):
        # Compute and return the perimeter (circumference) of the circle
        return abs(2 * pi * self.radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        # Initialize rectangle with given width and height
        self.width = width
        self.height = height

    def area(self):
        # Compute and return the area of the rectangle
        return self.width * self.height

    def perimeter(self):
        # Compute and return the perimeter of the rectangle
        return 2 * self.width + 2 * self.height


# Function that prints information about any shape-like object
# Assumes the object has .area() and .perimeter() methods (duck typing)
def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
