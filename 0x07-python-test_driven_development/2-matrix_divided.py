#!/usr/bin/python3
""" Divides each element ina matrix by the same value"""


def matrix_divided(matrix, div):
    """matrix_divided divides a matrix
    Args:
        matrix (int): A matrix of ints and floats
        div (int): The element to divide by
    Raises:
        TypeError: If matrix has non-numbers
        TypeError: If matrix rows vary in size
        TypeError: If if div is not a number
        ZeroDivisionError: if div = 0
    Return:
        A matrix containeing the results of the division
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(item, int) or isinstance(item, float))
                for item in [ele for row in matrix for ele in row])):
        raise TypeError('matrix must be a matrix (list of lists) of '
                        'integers/floats')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(x / div, 2) for x in row] for row in matrix]
