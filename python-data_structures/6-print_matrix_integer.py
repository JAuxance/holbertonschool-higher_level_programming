#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_elem = ["{:d}".format(x) for x in row]
        print(" ".join(formatted_elem) + "$")
