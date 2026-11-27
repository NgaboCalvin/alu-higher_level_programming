#!/usr/bin/python3
"""Module that defines a function to print indented text.

This module provides text_indentation, which prints a text
with two new lines after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """Print text with two new lines after . ? and :.

    Args:
        text: The text to print (str).

    Returns:
        None. Prints the indented text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
