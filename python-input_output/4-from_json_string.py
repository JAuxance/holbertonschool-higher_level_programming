#!/usr/bin/python3
"""
4-from_json_string.py
Returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to an object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
