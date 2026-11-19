#!/usr/bin/python3
"""6-square module - A square class with position support."""


class Square:
    """Square class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance with optional size and position."""
        if type(size) != int or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[0], bool) or isinstance(position[1], bool):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) != int or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], bool) or isinstance(value[1], bool):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square to stdout using # character."""
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("#" * self.__size)
