#!/usr/bin/python3
"""Module providing from_json_string."""
import json


def from_json_string(my_str):
    """Return the object represented by a JSON string."""
    return json.loads(my_str)
