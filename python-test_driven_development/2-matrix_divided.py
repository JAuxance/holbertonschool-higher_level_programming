#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module provides a function to divide all elements of a matrix
(list of lists of integers/floats) by a given divisor. The result
is a new matrix with all elements divided and rounded to 2 decimal places.

The function validates that:
    - The matrix is a list of lists of integers or floats
    - All rows have the same size
    - The divisor is a number (int or float)
    - The divisor is not zero
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists of integers or floats representing
                      the matrix to be divided.
        div (int, float): The number to divide all matrix elements by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix don't have the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is equal to zero.

    Returns:
        list: A new matrix with all elements divided by div and rounded
              to 2 decimal places.
    """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
