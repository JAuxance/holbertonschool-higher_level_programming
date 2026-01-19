#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        matrix_format = " ".join(["{}"] * len(row)) + "$"
        print(matrix_format.format(*row))

