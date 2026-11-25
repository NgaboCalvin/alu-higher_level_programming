#!/usr/bin/python3
"""Module providing append_write."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the number of characters."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
