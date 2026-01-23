#!/usr/bin/python3
"""module that defines a function to print text with specific indentation."""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end='')
        if text[i] in {'.', '?', ':'}:
            print('\n')
            while i + 1 < length and text[i + 1] == ' ':
                i += 1
        i += 1
