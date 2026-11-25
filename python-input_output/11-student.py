#!/usr/bin/python3
"""Module defining the Student class with reload support."""


class Student:
    """A student with basic public attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student."""
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return dict(self.__dict__)

    def reload_from_json(self, json):
        """Replace the student's attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
