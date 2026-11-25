#!/usr/bin/python3
"""Module providing load_from_json_file."""
import json


def load_from_json_file(filename):
    """Load an object from a JSON text file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
