#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module provides the add_integer function, which accepts
two numbers (integers or floats), validates their types,
and returns their sum as an integer.
"""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        int: The sum of a and b after casting to integers.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
