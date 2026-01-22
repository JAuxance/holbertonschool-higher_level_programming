#!/usr/bin/python3
"""Module that adds two integers or floats.
Defines a function add_integer that takes two parameters a and b,
which can be integers or floats, and returns their sum as an integer.
If the parameters are not integers or floats, it raises a TypeError."""


def add_integer(a, b=98):
    """Add two integers or floats.
    
    Args:
        a: An integer or float to add.
        b: An integer or float to add (default is 98).
    
    Returns:
        The sum of a and b as an integer.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
