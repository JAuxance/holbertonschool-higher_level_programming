#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r") as file:
        for line in file:
            print((line))
