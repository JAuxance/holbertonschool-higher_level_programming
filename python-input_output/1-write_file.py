#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w+") as file:
        return file.write(text)
