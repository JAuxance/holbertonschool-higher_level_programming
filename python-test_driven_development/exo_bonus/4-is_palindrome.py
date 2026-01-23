#!/usr/bin/python3
"""Module that defines a palindrome checking function."""


def is_palindrome(text):
    """Checks if a given string is a palindrome.
    Args:
        text (str): The string to check.
    Returns:
        bool: True if text is a palindrome, False otherwise.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    clean = text.replace(" ", "").lower()

    return clean == clean[::-1]
