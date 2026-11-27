#!/usr/bin/python3
"""Module defining the Square class.

This module provides the Square class, which inherits from
Rectangle and represents a square with equal sides.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class with size, x, y and id."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size (width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes using args or kwargs."""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, val in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == "size":
                        self.size = val
                    else:
                        setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                if key == "size" or key in ("width", "height"):
                    self.size = val
                elif key in ("id", "x", "y"):
                    setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
