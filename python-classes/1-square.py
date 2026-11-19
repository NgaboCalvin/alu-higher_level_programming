#!/usr/bin/python3
"""1-square module - A square class with private size attribute."""


class Square:
    """Square class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a Square instance with an optional size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
