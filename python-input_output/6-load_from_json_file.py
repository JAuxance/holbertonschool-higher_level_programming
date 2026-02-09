#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, "r")as f:
        return json.load(f)
