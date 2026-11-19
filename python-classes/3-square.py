#!/usr/bin/python3
"""3-square module - A square class with size validation and area method."""


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
        if type(size) != int or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
