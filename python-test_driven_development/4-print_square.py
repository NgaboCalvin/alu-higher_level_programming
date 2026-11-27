#!/usr/bin/python3
"""Module that defines a function to print a square.

This module provides print_square, which prints a square
made of the '#' character with the given side length.
"""


def print_square(size):
    """Print a square of size x size using '#'.

    Args:
        size: The side length of the square (int).

    Returns:
        None. Prints the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
