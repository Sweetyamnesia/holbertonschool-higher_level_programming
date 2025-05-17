#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number.

Args:
    matrix (list of lists of int/float): The matrix to divide.
    div (int or float): The number to divide by.

Returns:
    list of lists of float: A new matrix with each value divided by div,
    rounded to 2 decimal places.

Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
    TypeError: If rows in the matrix are not of the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is zero.
"""


def matrix_divided(matrix, div):
    result = []
    if not isinstance(matrix, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) "
            		    "of integers/floats")
    for each row in matrix:
        if length(row) != length(matrix):
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        if row != matrix:
            raise TypeError("Each row of the matrix "
                			"must have the same size")
    return result
