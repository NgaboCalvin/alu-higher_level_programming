#!/usr/bin/python3
"""Module providing class_to_json."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return dict(
        obj.__dict__)
