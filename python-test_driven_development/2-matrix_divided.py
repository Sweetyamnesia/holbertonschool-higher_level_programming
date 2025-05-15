#!/usr/bin/python3
"""
    Divide all elements of a matrix.

    Args:
    matrix: The first operand
    div: The second operand.

    Returns:
    a new matrix.

    Raises:
    TypeError: If matrix is neither a list of integers/float.
    TypeError: If matrix neither have the same size of each row.
    TypeError: If div is not a number.
    ZeroDivisionError: div can't be equal to 0
"""


def matrix_divided(matrix, div):
    result = []
    for row in matrix:
        if not isinstance(matrix, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) " \
            "of integers/floats")
        elif not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        else:
            if row != matrix:
                raise TypeError("Each row of the matrix " \
                "must have the same size")
    return result
