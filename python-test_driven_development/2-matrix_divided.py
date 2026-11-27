#!/usr/bin/python3
"""Module that defines a function to divide a matrix by a number.

This module provides matrix_divided, which divides every element
of a matrix (list of lists) by a given divisor and returns
a new matrix with values rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix: A list of lists of ints or floats.
        div: The divisor (int or float).

    Returns:
        list: A new matrix with each element divided by div
        and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is invalid, rows differ in size,
            or div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
