#!/usr/bin/python3
"""Module that defines a function to print a name.

This module provides say_my_name, which prints a formatted
string containing the first and last name provided.
"""


def say_my_name(first_name, last_name=""):
    """Print the full name in the format 'My name is ...'.

    Args:
        first_name: The first name (str).
        last_name: The last name (str), defaults to empty.

    Returns:
        None. Prints the formatted name.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
