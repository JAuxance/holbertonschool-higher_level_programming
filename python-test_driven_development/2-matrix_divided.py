#!/usr/bin/python3
"""module that divides all elements of a matrix.
Defines a function matrix_divided that takes a matrix (list of lists) and a divisor,
and returns a new matrix with each element divided by the divisor, rounded to 2 decimal places.
Raises appropriate exceptions for invalid inputs."""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (_type_): _description_
        div (_type_): _description_

    Raises:
        TypeError: _description_
        ZeroDivisionError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
