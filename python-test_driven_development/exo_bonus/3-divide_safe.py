#!/usr/bin/python3
"""Module that defines a safe division function."""


def divide_safe(a, b):
    """Divides two numbers safely.
    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.
    Returns:
        float: The result of the division a / b.
        If b is 0, returns 0 instead of raising an exception.
    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an int or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an int or float")
    if b == 0:
        return 0
    else:
        return (a / b)
