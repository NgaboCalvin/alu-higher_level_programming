#!/usr/bin/python3
"""Module defining the Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a validated size."""

    def __init__(self, size):
        """Initialize a square with a size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
