#!/usr/bin/python3
"""function that divides matrix by a number"""


def matrix_divided(matrix, div):
    """
    function that divides matrix by number; div
    matrix must be a list of lists of integers or floats
    div must be a non-zero integer or float
    """
    if not all(isinstance(i, list) for i in matrix):
        raise TypeError("matrix must \
be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the \
matrix must have the same size")
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = list(map(
        lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return new
