#!/usr/bin/python3
"""
0-read_file.py
Reads and prints the content of a text file (UTF8).
"""
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line)
