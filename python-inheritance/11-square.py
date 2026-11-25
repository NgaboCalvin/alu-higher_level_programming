#!/usr/bin/python3
"""Module defining the Square class with its description."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a validated size."""

    def __init__(self, size):
        """Initialize a square with a size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
