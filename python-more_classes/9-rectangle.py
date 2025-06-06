#!/usr/bin/python3
"""
This module defines a class named Rectangle.
It is a basic example to illustrate object-oriented programming in Python.
"""


class Rectangle:
    """
    Represents an empty rectangle.

    This is a placeholder class used to illustrate the structure
    of a class in Python.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width and height: The width and the height of the rectangle.
            Must be a non-negative integer

        Raises:
        TypeError: If width and height are not an integer.
        ValueError: If width and height are less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)

    def __str__(self):
        """
        Print the rectangle.

        Returns:
            The rectangle with character #.
        """
        if self.width == 0 or self.height == 0:
            return ""

        result = ""
        for i in range(self.height):
            result += str(self.print_symbol) * self.width
            if i != self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """
        Return a string representation of the rectangle and
        recreate a new instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        print message when instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
