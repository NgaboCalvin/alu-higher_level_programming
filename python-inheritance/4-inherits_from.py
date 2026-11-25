#!/usr/bin/python3
"""Module providing the inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class but is not exactly it."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
