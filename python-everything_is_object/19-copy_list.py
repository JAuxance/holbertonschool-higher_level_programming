#!/usr/bin/python3
"""Define a function that copies a list."""


def copy_list(a_list):
    """Return a copy of a list."""
    copy_list = []

    for item in a_list:
        copy_list.append(item)

    return copy_list
