#!/usr/bin/python3
"""Module defining the Student class."""


class Student:
    """A student with basic public attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the student."""
        return dict(self.__dict__)
