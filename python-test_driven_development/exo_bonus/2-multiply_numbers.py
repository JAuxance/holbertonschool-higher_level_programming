#!/usr/bin/python3
"""
    Docstring for hlb_proj.holbertonschool-higher_level_programming.python-test_driven_development.exo_bonus.2-multiply_numbers
    This module provides a function to multiply two numbers with type checking.
    """


def multiply_numbers(a, b=1):
    """
    Multiplies two numbers after validating their types.
    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 1.
    Returns:
        int or float: The product of a and b.
    Raises:
        TypeError: If a or b is not an int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an int or float")
    if type(b) not in (int, float):
        raise TypeError("b must be an int or float")
    return a * b
