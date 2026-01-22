#!/usr/bin/python3
"""Module that adds two integers or floats.
Defines a function add_integer that takes two parameters a and b,
which can be integers or floats, and returns their sum as an integer.
If the parameters are not integers or floats, it raises a TypeError."""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
