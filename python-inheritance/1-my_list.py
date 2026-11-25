#!/usr/bin/python3
"""Module defining the MyList class."""


class MyList(list):
    """A list subclass that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
