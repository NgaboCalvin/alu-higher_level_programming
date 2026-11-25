#!/usr/bin/python3
"""Module providing save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """Save an object as JSON in a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
